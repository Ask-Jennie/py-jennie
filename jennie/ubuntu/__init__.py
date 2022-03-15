import os, random, string
from jennie.ubuntu.config_builder import  *
from jennie.setup import  Setup

class Ubuntu():
    def __init__(self):
        self.init_library()

    def init_library(self):
        """
        Checks if User is logged in for the project. add proper output
        directory path. Also create a flag based on if library is present
        on server or not.
        """
        self.user_info = Setup().is_user_logged_in()
        self.token = self.user_info["token"]
        if not self.user_info:
            raise ValueError("User Not logged in.")

    def install_lemp(self):
        os.system("add-apt-repository universe")
        os.system("apt-get update")
        os.system("apt-get install nginx mysql-server php-fpm php-mysql php-mbstring php-gettext apache2-utils -y")
        os.system("ufw allow 'Nginx Full'")
        os.system("unlink /etc/nginx/sites-enabled/default")
        os.system("apt-get install libmysqlclient-dev -y")
        nginx_conf_file = create_nginx_config(
            domain="localhost", port="80", root="/usr/share/nginx/html", platform="html"
        )
        open("/etc/nginx/conf.d/localhost.conf", "w").write(nginx_conf_file)
        os.system("service php7.2-fpm start")

        os.system("sudo pip3 install uwsgi")
        os.system("sudo mkdir /etc/uwsgi")
        open("/etc/systemd/system/uwsgi.service", "w").write(UWSGI_CONF)

        password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        mysql_pass_change_command = mysql_password_change_command(
            "root", password
        )
        os.system(mysql_pass_change_command)
        print("Installed Nginx, MySQL, PHP \nNote Down MySQL DB Credentials: "
              "\n\tuser: root"
              "\n\tpassword: " + password)

    def install_certbot(self):
        os.system("add-apt-repository ppa:certbot/certbot")
        os.system("apt-get update")
        os.system("apt-get install python-certbot-nginx")

    def install_phpmyadmin(self, output_dir):
        os.chdir(path=output_dir)
        os.system("wget https://files.phpmyadmin.net/phpMyAdmin/5.1.0/phpMyAdmin-5.1.0-all-languages.tar.gz")
        os.system("tar -xvf phpMyAdmin-5.1.0-all-languages.tar.gz")
        os.system("mv phpMyAdmin-5.1.0-all-languages phpmyadmin")
        os.system("rm -rf phpMyAdmin-5.1.0-all-languages.tar.gz")

        nginx_conf_file = create_nginx_config(
            domain="localhost", port="8081", root=output_dir, platform="html"
        )
        open("/etc/nginx/conf.d/phpmyadmin.conf", "w").write(nginx_conf_file)
        os.system("systemctl reload nginx")

    def restart_uwsgi(self):
        if not os.path.isfile("/etc/systemd/system/uwsgi.service"):
            os.system("sudo pip3 install uwsgi")
            os.system("sudo mkdir /etc/uwsgi")
            open("/etc/systemd/system/uwsgi.service", "w").write(UWSGI_CONF)
            os.system("systemctl start uwsgi.service")
        else:
            os.system("systemctl restart uwsgi.service")

    def deploy_backend_django_project(self, domain, port, root, project_name, project_folder):
        if port == "443":
            self.install_certbot()
            os.system("sudo service nginx stop")
            os.system("certbot certonly --standalone -d {}".format(domain))
            os.system("sudo service nginx start")
        internal_port = str(random.randint(9091, 9999))
        nginx_conf_file = create_nginx_config(
            domain=domain, port=port, root="", platform="django", uwsgi_port=internal_port
        )
        file_name = project_name.replace(" ", "").replace("-", "").replace("_", "")
        open("/etc/nginx/conf.d/{}.conf".format(file_name), "w").write(nginx_conf_file)

        uwsgi_config_file = create_uwsgi_conf(root=root, internal_port=internal_port, project_name=project_name, project_folder=project_folder)
        open("/etc/uwsgi/{}.ini".format(file_name), "w").write(uwsgi_config_file)
        self.restart_uwsgi()
        os.system("sudo service nginx restart")

    def deploy_frontend_angular_project(self, domain, port, root):
        if port == "443":
            self.install_certbot()
            os.system("sudo certbot --nginx -d {}".format(domain))
        nginx_conf_file = create_nginx_config(
            domain=domain, port=port, root=root, platform="angular"
        )
        file_name = domain.replace(".", "")
        open("/etc/nginx/conf.d/{}.conf".format(file_name), "w").write(nginx_conf_file)
        os.system("sudo service nginx reload")

    def deploy_frontend_html_project(self, domain, port, root):
        if port == "443":
            self.install_certbot()
            os.system("sudo certbot --nginx -d {}".format(domain))
        nginx_conf_file = create_nginx_config(
            domain=domain, port=port, root=root, platform="html"
        )
        file_name = domain.replace(".", "")
        open("/etc/nginx/conf.d/{}.conf".format(file_name), "w").write(nginx_conf_file)
        os.system("sudo service nginx reload")
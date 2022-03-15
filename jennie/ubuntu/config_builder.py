NGINX_CONFIG = '''server {
CONF_HEADER
CONF_LOCATION        
}
'''

NGINX_CONF_HEADER_NORMAL_ANGULAR = '''
        listen PORT;
        listen [::]:PORT;
        index index.php index.html index.htm index.nginx-debian.html;
        server_name DOMAIN;

        charset     utf-8;
        client_max_body_size 75M;   # adjust to taste
'''

CONF_HEADER_SSL_ANGULAR = '''
        listen 443;
        listen [::]:443;
        index index.php index.html index.htm index.nginx-debian.html;
        server_name DOMAIN;

        ssl on;
        ssl_certificate  /etc/letsencrypt/live/DOMAIN/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/DOMAIN/privkey.pem;

        charset     utf-8;
        client_max_body_size 75M;   # adjust to taste
'''

NGINX_LOCATION_PHP = '''
        location ~ \.php$ {
            include snippets/fastcgi-php.conf;
            fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
        }
'''
NGINX_LOCATION_ANGULAR = '''
        location / {
            try_files $uri $uri/ =404;
        }
'''

NGINX_LOCATION_DJANGO = '''
        location / {
                uwsgi_pass  UPSTREAM_NAME;
                include     /etc/nginx/uwsgi_params;
        }
'''

DJANGO_UPSTREAM = '''
upstream UPSTREAM_NAME {
    server 127.0.0.1:INTERNAL_PORT;      # for a web port socket
}
'''


DEFAULT_UWSGI = '''[uwsgi]
project = PROJECT_NAME
base = ROOT

chdir = %(base)/PROJECT_FOLDER
module = %(project).wsgi:application

master = true
processes = 2
socket = 127.0.0.1:INTERNAL_PORT
chmod-socket = 664
vacum = true
daemonize = /var/log/PROJECT_NAME.log
py-autoreload = 1
'''
MYSQL_CHANGE_PASSWORD_COMMAND = '''mysql -u root --execute="ALTER USER 'MYSQL_USER'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MYSQL_PASSWORD';"'''


UWSGI_CONF = '''[Unit]
Description=uwsgi service
[Service]
User=root
WorkingDirectory=/usr/local/bin
ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi
[Install]
WantedBy=multi-user.target'''


def create_nginx_config(domain, port, root, platform=None, uwsgi_port=9005):
    nginx_conf = NGINX_CONFIG
    if port == "HTTP":
        port = "80"
    if port == "HTTPS":
        port = "443"

    if port == "443":
        CONF_HEADER = CONF_HEADER_SSL_ANGULAR.replace("DOMAIN", domain)
    else:
        CONF_HEADER = NGINX_CONF_HEADER_NORMAL_ANGULAR.replace("DOMAIN", domain)
        CONF_HEADER = CONF_HEADER.replace("PORT", port)

    if platform == "angular":
        CONF_HEADER += "\n        root {};".format(root)
        CONF_LOCATION = NGINX_LOCATION_ANGULAR
    elif platform == "django":

        UPSTREAM_NAME = domain.replace(".", "_")
        INTERNAL_PORT = uwsgi_port
        UPSTREAM_CONF = DJANGO_UPSTREAM.replace("UPSTREAM_NAME", UPSTREAM_NAME).replace("INTERNAL_PORT",
                                                                                        str(INTERNAL_PORT))
        CONF_LOCATION = NGINX_LOCATION_DJANGO.replace("UPSTREAM_NAME", UPSTREAM_NAME)
        nginx_conf = UPSTREAM_CONF + nginx_conf
    else:
        CONF_HEADER += "\n        root {};".format(root)
        CONF_LOCATION = NGINX_LOCATION_ANGULAR
        CONF_LOCATION += NGINX_LOCATION_PHP

    nginx_conf = nginx_conf.replace("CONF_HEADER", CONF_HEADER).replace("CONF_LOCATION", CONF_LOCATION)
    return nginx_conf

def create_uwsgi_conf(root, project_name, project_folder, internal_port):
    uwsgi_conf = DEFAULT_UWSGI.replace("ROOT", root)
    uwsgi_conf = uwsgi_conf.replace("INTERNAL_PORT", internal_port)
    uwsgi_conf = uwsgi_conf.replace("PROJECT_NAME", project_name)
    uwsgi_conf = uwsgi_conf.replace("PROJECT_FOLDER", project_folder)
    return uwsgi_conf

def mysql_password_change_command(username, password):
    command = MYSQL_CHANGE_PASSWORD_COMMAND.replace("MYSQL_PASSWORD", password).replace("MYSQL_USER", username)
    return command

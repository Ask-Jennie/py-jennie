from jennie.angular.helper import *

DOWNLOAD_LIB_INFO = "https://api.ask-jennie.com/v1/download_lib/"

class DownloadLib():
    def __init__(self, app_name=None):
        self.app_name = app_name
        self.token = get_user_access_token()["payload"]["token"]
        if self.token == None:
            raise ValueError("User not logged in, require login to upload library")

        self.curr_directory = os.getcwd()
        if self.curr_directory[:-1] != "/":
            self.curr_directory += "/"

    @property
    def download_ui_component(self):
        url = DOWNLOAD_LIB_INFO + "?app_name=" + self.app_name
        lib_info_resp = requests.get(url, headers={"token": self.token})
        jsonConf = create_angular_module_info(lib_info_resp.json()["payload"])
        app_name = jsonConf["app_name"]
        if check_if_angular_project(self.curr_directory):
            os.system("ng g c uigallery/{} --skip-tests=true".format(app_name))
            open("src/app/uigallery/{0}/{0}.component.css".format(app_name), "w").write(jsonConf["css_file_data"])
            open("src/app/uigallery/{0}/{0}.component.html".format(app_name), "w").write(jsonConf["html_file_data"])
            open("src/app/uigallery/{0}/{0}.component.ts".format(app_name), "w").write(jsonConf["ts_file_data"])
            scripts_attachment_html = ""
            for script in jsonConf["scripts"]:
                open("src/assets/{}".format(script), "w").write(jsonConf["scripts"][script])
                scripts_attachment_html += "<script src='assets/{}'></script>\n".format(script)
            index_html = open("src/index.html", "r").read()
            index_html = index_html.replace("</body>", scripts_attachment_html + "</body>")
            open("src/index.html", "w").write(index_html)
            return True
        else:
            print ("Not an angular project")
        return False

if __name__ == '__main__':
    status = DownloadLib("navbarlight").download_ui_component
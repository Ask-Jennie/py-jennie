import requests
from jennie.angular.helper import *

UI_LIB_API = "https://api.ask-jennie.com/v1/upload_lib/"
IMAGE_UPLOAD_API = "https://api.ask-jennie.com/v1/image_upload/"

class UploadLib():
    def __init__(self, directory=None, update=False):
        self.update = update
        if directory == None:
            self.curr_dir = os.getcwd()
        else:
            self.curr_dir = directory

        self.token = get_user_access_token()["payload"]["token"]
        if self.token == None:
            raise ValueError("User not logged in, require login to upload library")

    def get_extra_scripts(self, appinfo):
        if "scripts" in appinfo["jennie_conf"]:
            scripts = appinfo["jennie_conf"]
            for file in scripts:
                scripts[file.split("/")[-1]] = open(scripts[file]).read()
        else:
            scripts = {}
        return scripts

    def check_unique_component(self, app_name):
        url = UI_LIB_API + "?check_library=true&name=" + app_name
        api_check_res = requests.get(url, headers={"token": self.token})
        if not api_check_res.json()["payload"]["available"]:
            raise ValueError("Library name is already used, try different name")
        return True

    def check_if_component_exits(self, app_name):
        url = UI_LIB_API + "?check_library=true&name=" + app_name
        api_check_res = requests.get(url, headers={"token": self.token})
        if not api_check_res.json()["payload"]["available"]:
            return True
        raise ValueError("Library does not exits")

    def verify_json_conf(self, jsonconf, app_name):
        required_keys = ["type", "name", "title", "description", "image_file", "tag"]
        for key in required_keys:
            if key not in jsonconf:
                raise ValueError("Missing key {} in json configration".format(key))
        available_libraries_type = ["bootstrap-ui-gallery"]
        if jsonconf["type"] not in available_libraries_type:
            raise ValueError("Invalid Library type")

        if app_name != jsonconf["name"]:
            raise ValueError("App name doest matches with the name of component")
        return True

    def upload_lib_to_ask_jennie(self, data, update=False):
        """
        data: {
          "css_file_data": "CSS_FILE_DATA",
          "html_file_data": "HTML_FILE_DATA",
          "ts_file_data": "TS_FILE_DATA",
          "jennie_conf": {
            "type": "bootstrap-ui-gallery",
            "name": "component name, will be used to install component in angular",
            "title": "Title of library, will be displayed on UI ASK Jennie website",
            "description": "Description about the library"
          },
          "app_name": "component name, will be used to install component in angular",
          "scripts": {}
        }
        :return:
        """

        files = {'media': open(data["jennie_conf"]["image_file"], 'rb')}
        data["tag"] = data["jennie_conf"]["tag"]

        image_res = requests.post(IMAGE_UPLOAD_API, headers={"token": self.token}, files=files)
        del data["jennie_conf"]["image_file"]
        del data["jennie_conf"]["tag"]
        data["jennie_conf"]["image"] = image_res.json()["payload"]

        if update:
            api_res = requests.put(UI_LIB_API, headers={"token": self.token}, json=data)
        else:
            api_res = requests.post(UI_LIB_API, headers={"token": self.token}, json=data)
        return api_res

    def update_lib_to_ask_jennie(self, data):
        """
        data: {
          "css_file_data": "CSS_FILE_DATA",
          "html_file_data": "HTML_FILE_DATA",
          "ts_file_data": "TS_FILE_DATA",
          "jennie_conf": {
            "type": "bootstrap-ui-gallery",
            "name": "component name, will be used to install component in angular",
            "title": "Title of library, will be displayed on UI ASK Jennie website",
            "description": "Description about the library"
          },
          "app_name": "component name, will be used to install component in angular",
          "scripts": {}
        }
        :return:
        """

        files = {'media': open(data["jennie_conf"]["image_file"], 'rb')}
        data["tag"] = data["jennie_conf"]["tag"]

        image_res = requests.post(IMAGE_UPLOAD_API, headers={"token": self.token}, files=files)
        del data["jennie_conf"]["image_file"]
        del data["jennie_conf"]["tag"]
        data["jennie_conf"]["image"] = image_res.json()["payload"]
        api_res = requests.put(UI_LIB_API, headers={"token": self.token}, json=data)
        return api_res

    @property
    def upload_ui_component(self):
        """
        - Get module info
        - Get all scripts
        - if Verify JSON Config
            - Check if
        :return:
        """
        lib_info = get_angular_module_info(self.curr_dir)
        lib_info["scripts"] = self.get_extra_scripts(lib_info)
        lib_info["stack"] = "angular"
        if self.verify_json_conf(lib_info["jennie_conf"], lib_info["app_name"]):
            print ("Uploading Library....", json.dumps(lib_info, indent=2))

            if self.update:
                self.check_if_component_exits(app_name=lib_info["app_name"])
            else:
                self.check_unique_component(app_name=lib_info["app_name"])

            resp = self.upload_lib_to_ask_jennie(lib_info, self.update)
            if (resp.status_code == 201):
                return True
            raise ValueError("Unhandled Error")
        raise ValueError("Unhandled Error")
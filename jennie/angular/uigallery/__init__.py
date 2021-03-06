from jennie.setup import Setup
from jennie.jennie_tools import *
from jennie.angular.helper import *

class AngularUILibrary():
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
        self.out = os.getcwd()
        if not self.user_info:
            raise ValueError("User Not logged in.")

        if self.out[-1] != "/":
            self.out += "/"

        self.app_name = self.out.split("/")[-2]
        self.do_library_exits = does_angular_ui_gallery_exits(self.app_name, self.token)

    def update_library_module(self):
        """
        Check if library exits.
        Check if component files exits
        Create jennie configration
        Update information to Jennie Angular UI Module Server.
        :return:
        """
        if not self.do_library_exits:
            print ("Library does not exits")
            return False

        check_angular_ui_module_files(self.out)
        jennie_conf = create_angular_ui_module_conf(self.app_name, self.out, self.token)
        response = requests.put(
            "https://api.ask-jennie.com/v1/angular/ui-lib/",
            json=jennie_conf,
            headers={"token": self.user_info["token"]}
        ).json()
        return True

    def upload_library_module(self):
        """
        Check if component is proper.
        Get app name from component directory
        Check if component app name is unique and Jennie Angular UI Module Server
        Create Jennie Configration with uploaded file links.
        Call POST: https://api.ask-jennie.com/v1/angular/ui-lib/ with jennie conf
        Save Response back to jennie.conf.json
        """
        check_angular_ui_module_files(self.out)
        if self.do_library_exits:
            print("Library Already Exits")
            return False

        jennie_conf = create_angular_ui_module_conf(self.app_name, self.out, self.token)

        response = requests.post(
            "https://api.ask-jennie.com/v1/angular/ui-lib/",
            json=jennie_conf,
            headers={"token": self.user_info["token"]}
        ).json()

        if response["message"] == "Library already exits":
            print ("Library Already Exits")
            return

        with open('jennie.conf.json', 'w') as f:
            json.dump(response["payload"], f, ensure_ascii=False, indent=4)

        print ("Library Uploaded Successfully")
        return True

    def add_library_module(self, app_name):
        """
        Check if execution directory is Angular Project
        Get Angular UI Lib Information from API.
        Confirm if downloaded library is of type angular-ui-lib
        Generate Angular Component
        Update Component HTML, CSS, TS File with UI module files.
        If scripts are there add it to index.html
        """
        if not check_if_angular_project(directory=self.out):
            raise ValueError("Not an angular Project")

        response = requests.get("https://api.ask-jennie.com/v1/angular/ui-lib/?app_name=" + app_name,
            headers= { "token": self.user_info["token"] }
        ).json()
        resp_json = response["payload"]

        if resp_json["type"] == "angular-ui-lib":
            # generate component using ng command.
            module_create_command = "ng g c ui-gallery/{}".format(app_name)
            print ("Creating Component For Module")
            os.system(module_create_command)
            output_dir = "src/app/ui-gallery/{}/".format(app_name)

            print("\nUpdating Code...")
            download_and_update_ui_module_files(resp_json, output_dir)

        else:
            raise ValueError("Unknown Angular UI gallery type, ensure using external verified libraries")


    def delete_library_module(self, app_name):
        """
        Check if execution directory is Angular Project
        Get Angular UI Lib Information from API.
        Confirm if downloaded library is of type angular-ui-lib
        Generate Angular Component
        Update Component HTML, CSS, TS File with UI module files.
        If scripts are there add it to index.html
        """
        response = requests.delete(
            "https://api.ask-jennie.com/v1/angular/ui-lib/",
            json={ "app_name": app_name },
            headers= { "token": self.user_info["token"] }
        ).json()
        if not response["payload"]:
            print (response["message"])
        else:
            print (response["payload"])
import os, requests
from os.path import isfile, join

def does_angular_ui_gallery_exits(app_name, token):
    """
    Validates the existence of app on jennie server
    :param app_name: Name to validate
    :param token: User Token
    :return: boolean
    """
    response = requests.get("https://api.ask-jennie.com/v1/angular/ui-lib/validate/?app_name=" + app_name,
        headers={"token": token}
    ).js

    if not response["payload"]:
        return False
    return True

def check_if_angular_project(directory):
    """
    Check if directory is an angular project
    :param directory: directory path
    :return: Boolean
    """
    if directory[-1] != "/":
        directory += "/"
    search_files = [
        "angular.json", "karma.conf.js",
        "package.json"
    ]
    print("Checking Project Type Directory for ", directory)
    is_angular = True
    for file in search_files:
        if not os.path.isfile(directory + file):
            is_angular = False

    return is_angular

def check_angular_ui_module_files(directory):
    """
    Check if directory contain files releated to angular ui module
    :param directory: directory to search for
    :return: Files or raise error.
    """
    component_name = directory.split("/")[-1]
    if len(component_name) < 3:
        component_name = directory.split("/")[-2]
    files = [f for f in os.listdir(directory) if isfile(join(directory, f))]
    if component_name + ".component.ts" not in files:
        raise ValueError("Missing TS file for the component")
    elif component_name + ".component.css" not in files:
        raise ValueError("Missing CSS file for the component")
    elif component_name + ".component.html" not in files:
        raise ValueError("Missing CSS file for the component")
    return files
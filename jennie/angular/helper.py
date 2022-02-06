import json
import os, requests
from os import listdir
from os.path import isfile, join
from jennie.responses import *
from jennie.setup import get_user_access_token

def check_if_angular_project(directory):
    search_files = [
        "angular.json", "karma.conf.js",
        "package.json"
    ]
    print ("Checking Project Type Directory for ", directory)
    is_angular = True
    for file in search_files:
        if not os.path.isfile(directory + file):
            is_angular = False

    return is_angular


def check_app_name(app_name, file):
    if (app_name == None):
        app_name = file.split(".component.")[0]
    elif app_name != file.split(".component.")[0]:
        raise ValueError("Invalid Angular Component")
    return app_name

def get_angular_module_info(directory):
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    css_found, html_found, ts_found, json_conf_found = False, False, False, False
    app_name = None

    for file in files:
        if "component.css" in file:
            app_name = check_app_name(app_name, file)
            css_found = True
        elif "component.html" in file:
            app_name = check_app_name(app_name, file)
            html_found = True

        elif "component.ts" in file:
            app_name = check_app_name(app_name, file)
            ts_found = True

        elif file == "jennie.conf.json":
            json_conf_found = True

    response = {}

    if directory[-1] != "/":
        directory = directory + "/"

    if not css_found:
        raise ValueError(MISSING_CSS_FILE)
    else:
        response["css_file_data"] = open(directory + app_name + ".component.css").read()

    if not html_found:
        raise ValueError(MISSING_HTML_FILE)
    else:
        response["html_file_data"] = open(directory + app_name + ".component.html").read()

    if not ts_found:
        raise ValueError(MISSING_TS_FILE)
    else:
        response["ts_file_data"] = open(directory + app_name + ".component.ts").read()

    if not json_conf_found:
        raise ValueError(MISSING_ASK_JENNIE_FILE)
    else:
        response["jennie_conf"] = json.loads(open(directory + "jennie.conf.json").read())

    response["app_name"] = app_name
    return response

def get_data_for_angular_ui_module(jsonInfo):
    jsonInfo["html_file_data"] = requests.get(jsonInfo["html_file_path"]).text
    jsonInfo["css_file_data"] = requests.get(jsonInfo["css_file_path"]).text
    jsonInfo["ts_file_data"] = requests.get(jsonInfo["ts_file_path"]).text
    if "scripts" in jsonInfo["jennie_conf"]:
        for script in jsonInfo["scripts"]:
            jsonInfo["scripts"][script] = requests.get(jsonInfo["scripts"][script]).text
    return jsonInfo

if __name__ == '__main__':
    status = get_angular_module_info("/Users/saurabhpandey/Desktop/ASKJennie/uigallery/src/app/home")
    print (status)

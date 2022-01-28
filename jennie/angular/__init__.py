import os
from jennie.angular.uigallery.uploadlib import UploadLib
from jennie.angular.uigallery.downloadlib import DownloadLib
from jennie.angular.helper import check_if_angular_project
from jennie.responses import UNKNOWN_PROJECT_TYPE
from jennie.api_calls import APICalls
from jennie.setup import get_user_access_token, get_dummy_user_access_token

def upload_library():
    """
    Upload Angular Component as library on Jennie Server.
    Shell command : jennie angular upload ui-lib
    :return: upload status
    """
    status = UploadLib().upload_ui_component
    print("Uploaded UI Component Successful")
    return status

def install_library(app_name):
    """
    Download Angular Component from Jennie Server and Install in Angular project.
    Upload Angular Component as library on Jennie Server.
    Shell command : jennie angular install libraryname
    :param app_name:
    :return:
    """
    status = DownloadLib(app_name=app_name).download_ui_component
    if status:
        print("UI Component Added Successfully\nComponent Tag: <app-{0}>/<app-{0}>".format(app_name))

def install_bootstrap():
    """
    Install Bootstrap and Jquery in the projects.
    Shell command : jennie angular install bootstrap
    :return:
    """
    current_dir = os.getcwd()
    if current_dir[:-1] != "/":
        current_dir += "/"

    if check_if_angular_project(current_dir):
        replace = "</head>"
        replace_with = '''  <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css" rel="stylesheet">  
</head>'''
        replace_for_script = "</body>"
        replace_for_script_with = '''  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.min.js"></script>
</body>'''
        dataset = open(current_dir + "src/index.html", "r").read()
        dataset = dataset.replace(replace, replace_with)
        dataset = dataset.replace(replace_for_script, replace_for_script_with)
        open(current_dir + "src/index.html", "w").write(dataset)
    else:
        print (UNKNOWN_PROJECT_TYPE)


def create_login_signup_project(config):
    # token = get_user_access_token()["payload"]["token"]
    token = get_dummy_user_access_token()["payload"]["token"]
    headers = { "token": token }
    res = APICalls().post(url="https://api.ask-jennie.com/v1/app/create-angular-login-signup-app/", headers=headers, body=config)
    print (res)


def create_crm_project(config):
    # token = get_user_access_token()["payload"]["token"]
    token = get_dummy_user_access_token()["payload"]["token"]
    headers = { "token": token }
    # res = APICalls().post(url="https://api.ask-jennie.com/v1/app/create-angular-login-signup-app/", headers=headers, body=config)
    response = {
        "app_code": "{'project_link': 'https://projects.ask-jennie.com/1643231549-5272305.zip'",
        "pre_commands": ["ng g new {}".format(config["project_name"]), "cd {}".format(config["project_name"])],
        "post_commands": ["npm i"]
    }
    print ("Angular Login Project Ready To Use.")
    print (response)


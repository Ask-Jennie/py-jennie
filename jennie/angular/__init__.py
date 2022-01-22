import os
from jennie.angular.uigallery.uploadlib import UploadLib
from jennie.angular.uigallery.downloadlib import DownloadLib
from jennie.angular.helper import check_if_angular_project
from jennie.responses import UNKNOWN_PROJECT_TYPE

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
        print("UI Component Added Successfully Successfully")

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
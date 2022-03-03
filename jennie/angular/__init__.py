from jennie.angular.helper import check_if_angular_project
from jennie.angular.automations import *
from jennie.angular.uigallery import AngularUILibrary

def upload_library():
    """
    Upload Angular Component as library on Jennie Server.
    Shell command : jennie angular upload ui-lib
    :return: upload status
    """
    # status = UploadLib().upload_ui_component
    AngularUILibrary().upload_library_module()
    return True

def update_library():
    """
    Update Angular Component on Jennie Server.
    Shell command : jennie angular update ui-lib
    :return: upload status
    """
    AngularUILibrary().update_library_module()
    return True

def install_angular_ui_lib(app_name):
    """
    Download Angular Component from Jennie Server and Install in Angular project.
    Upload Angular Component as library on Jennie Server.
    Shell command : jennie angular install libraryname
    :param app_name:
    :return:
    """

    status = AngularUILibrary().add_library_module(app_name=app_name)
    if status:
        print("UI Component Added Successfully\nComponent Tag: <app-{0}>/<app-{0}>".format(app_name))

def delete_angular_ui_lib():
    status = AngularUILibrary().delete_library_module()

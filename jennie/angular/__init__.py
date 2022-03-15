from jennie.angular.uigallery import AngularUILibrary
from jennie.angular.automations import AngularAutomations

def upload_library():
    """
    Upload Angular Component as library on Jennie Server.
    Process :
    - Takes UI Modules details
        Title : Some title for the library, maximum 100 characters
        Description: A little bit about library, maximum 200 characters
        Image Path: Path of image.
        Tag: Tag associated to UI Module, optional, can be skipped.
    - Upload All UI Module Files to Jennie S3 Server, and jennie.conf.json is created with the details
    - Upload Jennie.conf.json to Jennie Backend Server.
    :important: make sure the folder must contain ( *.component.ts, *.component.css, *.component.html )
    Shell command : jennie angular upload ui-lib
    :return: upload status
    """
    status = AngularUILibrary().upload_library_module()
    return status

def update_library():
    """
    Update already uploaded Component on Jennie Server
    Process :
    - Takes Updated UI Modules details
        Title : Some title for the library, maximum 100 characters
        Description: A little bit about library, maximum 200 characters
        Image Path: Path of image.
        Tag: Tag associated to UI Module, optional, can be skipped.
    - Update All UI Module Files to Jennie S3 Server, and jennie.conf.json is created with the details
    - Upload updated jennie.conf.json to Jennie Backend Server.
    :important: make sure the folder must contain ( *.component.ts, *.component.css, *.component.html, jennie.conf.json )
    Shell command : jennie angular update ui-lib
    :return: upload status
    """
    status = AngularUILibrary().update_library_module()
    return status

def install_angular_ui_lib(app_name):
    """
    Download Angular Component Configration from Jennie Server and Install in Angular Modules
    inside Angular project. The command should be executed from an Angular Project Library

    Shell command : jennie angular download ui-lib <UI-MODULE-NAME>
    :param app_name:
    :return:
    """

    status = AngularUILibrary().add_library_module(app_name=app_name)
    return status


def delete_angular_ui_lib(app_name):
    """
    Delete Angular Component From Jennie Server.
    Shell command : jennie angular delete ui-lib <UI-MODULE-NAME>
    :return:
    """
    status = AngularUILibrary().delete_library_module(app_name)
    return status


def upload_angular_automations():
    """
    Upload Angular Automation Configration To Server, this include uploading
    information with all included files. make sure jennie.conf.json having
    information about automation should be present inside the folder.
    Shell command: jennie angular upload automations
    :return: Upload Status
    """

    status = AngularAutomations().upload_automation()
    return status

def update_angular_automations():
    """
    Update Angular Automation Configration To Server, this include updating
    information with all included files. make sure jennie.conf.json should
    be present inside the folder.

    Shell command: jennie angular upload automations
    :return: Update Status
    """
    status = AngularAutomations().update_automation()
    return status

def delete_angular_automations(automation_name):
    """
    Delete Angular automation from Jennie server.
    Shell command: jennie angular delete automations
    :return: Delete Status
    """
    status = AngularAutomations().delete_automation(automation_name)
    return status

def install_angular_automation(automation_name):
    """
    Get Angular Automation Configration from Jennie Backend Server,
    Install Automation inside Angular project, command must be executed
    from an Angular Project Library.
    :return: Automation Status
    """
    status = AngularAutomations().execute_automation(automation_name=automation_name)
    return status
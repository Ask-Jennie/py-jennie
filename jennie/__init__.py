"""
About The Tool
Jennie is a software tool that provide automation for different platform and frameworks.
The base idea of Jennie is to automate stardard task involved in the process of application development.

Release 0.0.1
Release contain automation related to Angular and Django with UI template gallery for Angular Framework.

Angular Automations

### Installing Bootstrap with jquery inside Angular Project
Bootstrap and Jquery are the libraries that helps any developer for frontend ui development.
The command automates the installation of these two library inside an angular project

Go inside the project and execute below command
    jennie angular install bootstrap

### Adding Dashboard Theme Structure in Angular Project.

Dashboard Theme Structure is referred to structure where pages are hidden behind login.
Once User logs in he can view other pages on the dashboard.
User session is also created.
The command execute below task
- creates login, signup, reset password page in the project.
- create AuthGaurd, SessionManager and Dummy Login Signup and Reset Password API Controller.
- Create Dashboard modules and inside dashboard module dashboard component is created. This dashboard component will show all sub pages.
- Creates Home Component and add it to Dashboard module and route it to /home.
- Add AuthGaurd to dashboard component so pages inside dashboard component can be accessed only after user has logged in

Go inside the project and execute below command
    jennie angular add dashboard-theme

### Adding User Session inside Angular Project.
Create AuthGaurd, SessionManager inside the angular project

Go inside the project and execute below command
    jennie angular add user-session

### Installing Firebase in Angular project

Firebase is a Backend-as-a-Service (Baas). It provides developers with a
variety of tools and services to help them develop quality apps,
Although Firebase integration is a little complex inside Angular Project.

The command automates the integration part.
Make sure you are inside angular project while executing the command
    jennie angular install firebase

### Create Table View inside Project for a specific DB table.

Table View for a DB table is referred to a component that has table to
represents entries from Db Table and had option to add, modify and delete entries.

The command takes configration as input that contains api information.
Base on information all for API method ( GET, POST, PUT, DELETE ) are implemented.
Table is added which is then attached to GET api that fetches information from DB table.
And models for Add, Modify and Delete events are also added on the page.

Make sure you are inside angular project while executing the command
    jennie angular add table-view path/to/table.json


"""
import sys
from jennie.setup import Setup
from jennie.angular import *
from jennie.ubuntu import *

__version__ = '0.0.1'
__author__ = 'ASK Jennie Developer <saurabh@ask-jennie.com>'
__description__ = 'The package targets protocol for uploading and reusing task and libraries'

def execute():

    if sys.argv[1] == "--version":
        Setup().show_version(__version__, __author__, __description__)

    elif sys.argv[1] == "logout":
        Setup().logout()

    elif sys.argv[1] == "setup":
        Setup().setup(sys.argv[2])

    # Ubuntu Automations starts here

    elif sys.argv[1] == "ubuntu" and sys.argv[2] == "install" and sys.argv[3] == "lemp":
        Ubuntu().install_lemp()

    elif sys.argv[1] == "ubuntu" and sys.argv[2] == "install" and sys.argv[3] == "phpmyadmin":
        Ubuntu().install_phpmyadmin(sys.argv[4])

    # Angular UI Lib starts here

    elif sys.argv[1] == "angular" and sys.argv[2] == "upload" and sys.argv[3] == "ui-lib":
        upload_library()

    elif sys.argv[1] == "angular" and sys.argv[2] == "update" and sys.argv[3] == "ui-lib":
        update_library()

    elif sys.argv[1] == "angular" and sys.argv[2] == "download" and sys.argv[3] == "ui-lib":
        install_angular_ui_lib(sys.argv[4])

    elif sys.argv[1] == "angular" and sys.argv[2] == "delete" and sys.argv[3] == "ui-lib":
        delete_angular_ui_lib(sys.argv[4])

    # Angular Automations starts here

    elif sys.argv[1] == "angular" and sys.argv[2] == "upload" and sys.argv[3] == "automation":
        upload_angular_automations()

    elif sys.argv[1] == "angular" and sys.argv[2] == "update" and sys.argv[3] == "automation":
        update_angular_automations()

    elif sys.argv[1] == "angular" and sys.argv[2] == "delete" and sys.argv[3] == "automation":
        delete_angular_automations(sys.argv[4])

    elif sys.argv[1] == "angular" and sys.argv[2] == "download" and sys.argv[3] == "automation":
        install_angular_automation(sys.argv[4])
    else:
        command = ' '.join(sys.argv)
        print ("Invalid command: {}, check jennie command list".format(command))

if __name__ == '__main__':
    execute()
"""
Shell Commands
    jennie setup
    jennie logout
    jennie install bootstrap
    jennie angular upload bootstrap-ui-lib
    jennie angular add ui-lib-name
"""
import sys
from jennie.tasklist import install_bootstrap
from jennie.setup import Setup
from jennie.angular.uigallery.uploadlib import Upload

__version__ = '0.0.1'
__author__ = 'ASK Jennie Developer <saurabh@ask-jennie.com>'

def execute():
    if sys.argv[1] == "logout":
        status = Setup().logout
        if (status):
            print ("Logged out successfully")
        else:
            print ("Unable to logout, try again")

    elif sys.argv[1] == "setup":
        Setup().setup(sys.argv[2])

    elif sys.argv[1] == "angular" and sys.argv[2] == "install" and sys.argv[3] == "bootstrap":
        install_bootstrap()

    elif sys.argv[1] == "angular" and sys.argv[2] == "upload":
        allowed = ["bootstrap-ui-lib"]
        if sys.argv[3] in allowed:
            Upload().upload_ui_component()
        else:
            print("Unknown Angular Library Type")

    elif sys.argv[1] == "angular" and sys.argv[2] == "add":
        Upload().download_ui_component()
        print ("Module successfully added to your project")

    else:
        command = ' '.join(sys.argv)
        print ("Invalid command: {}, check jennie command list".format(command))

if __name__ == '__main__':
    execute()
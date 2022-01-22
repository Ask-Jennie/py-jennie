"""
Shell Commands
    jennie setup
    jennie logout
    jennie angular upload ui-lib
    jennie angular install bootstrap
    jennie angular install uilibname
"""
import sys
from jennie.setup import Setup
from jennie.angular import upload_library, install_library, install_bootstrap

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

    elif sys.argv[1] == "angular" and sys.argv[2] == "upload" and sys.argv[3] == "ui-lib":
        upload_library()

    elif sys.argv[1] == "angular" and sys.argv[2] == "install":
        if sys.argv[3] == "bootstrap":
            install_bootstrap()
        else:
            install_library(sys.argv[3])
    else:
        command = ' '.join(sys.argv)
        print ("Invalid command: {}, check jennie command list".format(command))

if __name__ == '__main__':
    execute()
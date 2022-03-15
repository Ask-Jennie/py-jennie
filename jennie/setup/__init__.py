import json, sys, os
from getpass import getpass
from jennie.api_calls import APICalls

LOGIN_API = "https://api.ask-jennie.com/v1/login/"

home = os.path.expanduser("~")
if home[-1] != "/":
    home += "/"
TOKEN_PATH = home + ".token.json"

def get_user_access_token():
    if not os.path.isfile(TOKEN_PATH):
        return None
    return json.loads(open(TOKEN_PATH, "r").read())

class Setup():
    def __init__(self):
        self.state = 0

    def show_version(self, __version__, __author__, __description__):
        print ("Version :",__version__)
        print ("Author :",__author__)

        print(__description__ + "\n")
        user_info = self.is_user_logged_in()
        if (user_info == None):
            print ("Not logged in, To use the software try login using jennie setup [registered_email]")
            return
        print("User Name :", user_info["fullname"])
        print("User Email :", user_info["email"])

        print ("\nVersion Info : ")
        print ("Stable Version :", user_info["stable"])
        print ("Latest Version :", user_info["latest"])

    def is_user_logged_in(self):
        user_saved_info = None
        userinfo = get_user_access_token()
        if userinfo != None:
            user_saved_info = userinfo["payload"]
        return user_saved_info

    def login_to_ask_jennie(self, email, password):
        response = APICalls().post(
            url=LOGIN_API,
            body={"email": email, "password": password}
        )
        if (response["payload"] == None):
            print (response["message"])
            return False

        with open(TOKEN_PATH, 'w') as f:
            json.dump(response, f)

        print ("User Logged In Successfully")
        return True

    def setup(self, email):
        self.email = email
        token_info = self.is_user_logged_in()
        if (token_info):
            raise ValueError("User already logged in, try logout to resetup ( jennie logout ) ")
        else:
            print ("Continue Login, Enter Information")
            print ("Input Password for ASK Jennie Email:  ", self.email)
            password = getpass()
            return self.login_to_ask_jennie (self.email, password)

    def logout(self):
        if (self.is_user_logged_in() != None):
            command = "rm -rf {}".format(TOKEN_PATH)
            os.system(command)
            print ("Logged out successfully")
        else:
            print ("User not logged in")
        return True
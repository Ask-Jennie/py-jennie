import json, sys, os
from getpass import getpass
from jennie.api_calls import APICalls

LOGIN_API = "https://api.ask-jennie.com/v1/login/"
TOKEN_PATH = str(sys.executable).split("/bin/python")[0] + "/lib/python3.7/site-packages/jennie/" + "token.json"

def get_user_access_token():
    if not os.path.isfile(TOKEN_PATH):
        return None
    return json.loads(open(TOKEN_PATH, "r").read())

class Setup():
    def __init__(self):
        self.state = 0

    def login_to_ask_jennie(self, email, password):
        response = APICalls().post(
            url=LOGIN_API,
            body={"email": email, "password": password}
        )

        with open(TOKEN_PATH, 'w') as f:
            json.dump(response, f)

    def get_state(self):
        if (get_user_access_token() == None):
            return False
        return True

    def setup(self, email):
        self.email = email
        token_info = self.get_state()
        if (token_info):
            raise ValueError("User already logged in, try logout to resetup ( jennie logout ) ")
        else:
            print ("Continue Login, Enter Information")
            print ("Input Password for ASK Jennie Email:  ", self.email)
            password = getpass()
            self.login_to_ask_jennie (self.email, password)
        return True

    @property
    def logout(self):
        command = "rm -rf {}".format(TOKEN_PATH)
        os.system(command)
        return True
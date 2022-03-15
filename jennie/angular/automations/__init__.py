"""
General Automation protocol

automation = [
    {
        "type": "download_files",
        "files": {
            "output_dir": "filepath",
            "output_dir_1": "filepath_1",
        }
    },
    {
        "type": "shell_command",
        "commands": [
            "npm i"
        ]
    },
    {
        "type": "ui-lib",
        "libraries": [
            "bootstraploginpage", "bootstrapsignuppage", "bootstrapresetpasswordpage",
        ]
    }
    {
        "type": "angular-automations",
        "automations": [
            "user-session", "dummy-login-signup-apiservice", "dashboard-module AuthGuard=True"
        ]
    },
    {
        "type": "add_routing",
        "component": "",
        "path": "",
        "AuthGaurd": false
    },
    {
        "type": "index_script",
        "script": [ "script_path", "scripts_2_path" ]
    }
    {
        "type": "index_css"
        "script": [ "css_path", "css_2_path" ]
    }
]

"""


class AngularAutomations():
    def update_automation(self):
        automation_configration_file = open("jennie.conf.json", "r").read()
        return True

    def delete_automation(self, automation_name):
        return True

    def execute_automation(self, automation_name):
        response = { "automation": [
            {
                "type": "update_app_module",
                "update": [{
                    "type": "imports",
                    "import_name": "HttpClientModule",
                    "import_path": "import { HttpClientModule } from '@angular/common/http';"
                }]
            }
        ], "printed_response": '''Http Module added successfully\nYou can start using automation by importing `HttpClient` im your component''' }
        return True

    def upload_automation(self):
        automation_configration_file = open("jennie.conf.json", "r").read()
        return True

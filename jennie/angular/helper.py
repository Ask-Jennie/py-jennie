import json
from jennie.userinput import UserInput
from jennie.filehandler import upload_angular_ui_component, upload_image
from jennie.filehandler import add_file_from_link, add_script_to_angular_index_html

def create_angular_ui_module_conf(app_name, output_directory, token):
    """
    Get Title, Description, Image path, Tag from User.
    Upload Angular UI Component files.
    Create Jennie Conf
    :param app_name: App name to create Angular UI Module Conf
    :param output_directory: Directory to upload
    :param token: User Token
    :return: jennie conf
    """
    user_inputs = {
        "app_title": "Title for UI module", "app_description": "Description for UI module",
        "app_image": "Image file path, complete path of image", "tag": "Tag (optional) for module",
    }
    user_inputs = UserInput().take_user_input(user_inputs)
    resp = upload_angular_ui_component(app_name, output_directory, token)
    image_path = upload_image(user_inputs["app_image"], token)["image_link"]
    jennie_conf = {
        "css_file_path": "", "ts_file_path": "", "html_file_path": "",
        "scripts": {}, "app_name": app_name, "tag": user_inputs["tag"],
        "stack": "angular", "app_image": image_path, "app_title": user_inputs["app_title"],
        "app_description": user_inputs["app_description"], "type": "angular-ui-lib"
    }
    for key in resp:
        if "component.css" in key:
            jennie_conf["css_file_path"] = resp[key]
            print("Uploaded CSS File")
        elif "component.html" in key:
            jennie_conf["html_file_path"] = resp[key]
            print("Uploaded HTML File")
        elif "component.ts" in key:
            jennie_conf["ts_file_path"] = resp[key]
            print("Uploaded TS File")

    with open('jennie.conf.json', 'w') as f:
        json.dump(jennie_conf, f, ensure_ascii=False, indent=4)

    return jennie_conf

def download_and_update_ui_module_files(resp_json, output_dir):
    """
    Download Files related to ui modules from api
    response and update the same to output directory
    :param resp_json: JSON response for UI Module
    :param output_dir: Output Directory.
    :return: True
    """
    css_file_path, ts_file_path = resp_json["css_file_path"], resp_json["ts_file_path"]
    html_file_path, scripts = resp_json["html_file_path"], json.loads(resp_json["scripts"])
    add_file_from_link(html_file_path, output_dir)
    add_file_from_link(css_file_path, output_dir)
    add_file_from_link(ts_file_path, output_dir)

    # add scripts to index.html
    for script_path in scripts:
        script_link = scripts[script_path]
        add_file_from_link(script_link, script_path)
        add_script_to_angular_index_html(script_path)

    print("UI Component Added Successfully\nComponent Tag: <app-{0}>/<app-{0}>".format(resp_json["app_name"]))
    return True

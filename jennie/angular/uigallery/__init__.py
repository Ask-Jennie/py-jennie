"""
Angular UI Component Gallery Protocol

    In general the protocol upload snapshot of any angular component as ui gallery and upload it to jennie server
    Later the snapshot can be used in project.
    The protocol takes cares of all event involved between collecting information and uploading to JENNIE server and the
    other side involving the downloading and reusing of component

Upload :
    The upload protocol involves checking if working directory is a jennie angular component directory
    with *.component.ts, *.component.css, *.component.html and jennie.conf.json, once validated
    it collects information from jennie.conf.json about the gallery and uploads the information to

    Also it uploads local file from jennie.conf.json to JENNIE server and later used as IMAGE_FILE_LINK

    ASK Jennie UI gallery Server in form of json.
    {
        "css_file_data": "CSS_FILE_COPIED_FROM_FOLDER",
        "html_file_data": "HTML_FILE_COPIED_FROM_FOLDER",
        "ts_file_data": "TS_FILE_COPIED_FROM_FOLDER",
        "jennie_conf": {
            "type": jennie.conf.json["type"]
            "name": jennie.conf.json["name"],
            "title": jennie.conf.json["title"],
            "description": jennie.conf.json["description"],
            "image": "IMAGE_FILE_LINK"
        },
        "app_name": "component name, will be used to install component in angular",
    }

Download :
    The download protocol check if command is executed from angular project, once validated
    download information from api

    {
        "css_file_data": "CSS_FILE_DATA",
        "html_file_data": "HTML_FILE_DATA",
        "ts_file_data": "TS_FILE_DATA",
        "jennie_conf": {
            "type": jennie.conf.json["type"]
                "name": jennie.conf.json["name"],
                "title": jennie.conf.json["title"],
                "description": jennie.conf.json["description"],
                "image": "IMAGE_FILE_LINK"
            },
        "app_name": "component name",
    }

    and creates a component with app_name, and add css_file_data, html_file_data, ts_file_data data in component

    later the component can be use
    <app-app_name></app-app_name>
"""

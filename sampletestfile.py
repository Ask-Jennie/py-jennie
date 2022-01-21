from jennie.upload_angular_library import UploadAngularLibrary

json_conf = {
    "type": "bootstrap-ui-gallery",
    "name": "navbar-light",
    "title": "Bootstrap Standard Library",
    "pre-executed-commands": [
        "ng g c uigallery/navbarlight --skip-tests=true"
    ],
    "inputs": [],
    "html_file": "/Users/saurabhpandey/Desktop/ASKJennie/sindhuraconstructions/src/app/uigallery/navbarlight/navbarlight.component.html"
}
status = UploadAngularLibrary(json_conf).upload_library
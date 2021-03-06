# Jennie
The package targets protocol for uploading and reusing task and libraries. To Use the package one must be logged in. Follow setup process.

## Setup

Setup include login and logout, login using
- `For Login`: `jennie setup [register-email-address]`
- `For Logout`: `jennie logout`


### Angular UI Module Protocol

**- Download**


*A list of UI galleries can be found at [angular.uigallery.ask-jennie.com](https://angular.uigallery.ask-jennie.com/)*

To add any UI module to you angular project use
 
```
jennie angular download ui-lib <lib-name>
```

*output*
```
Checking Project Type 
Creating Component For Module
CREATE src/app/ui-gallery/bootstrapbreadcrumb/bootstrapbreadcrumb.component.css (0 bytes)
CREATE src/app/ui-gallery/bootstrapbreadcrumb/bootstrapbreadcrumb.component.html (34 bytes)
CREATE src/app/ui-gallery/bootstrapbreadcrumb/bootstrapbreadcrumb.component.spec.ts (717 bytes)
CREATE src/app/ui-gallery/bootstrapbreadcrumb/bootstrapbreadcrumb.component.ts (327 bytes)
```

*Make sure the command is executed inside an angular project.*

**- Upload**

User can also upload their custom made UI module to Jennie for later use.
 
```
jennie angular upload ui-lib
```

**Output**
```
Title for UI module
>> [Input Title for module and press enter, not more than 100 character]
Description for UI module
>> [Input Description for module and press enter, not more than 200 characters]
Image file path, complete path of image
>> [COPY & PASTE complete image path].
Tag (optional) for module
>> [OPTIONAL FIELD, select from list of tags or use your own].
Uploaded TS File
Uploaded CSS File
Uploaded HTML File
Library Uploaded Successfully
```

Once library is uploaded, json Info related to library can be seen inside jennie.conf.json

```json
{
    "_id": 32,
    "css_file_path": "https://ui-gallery.s3.ap-south-1.amazonaws.com/angular/ui-lib/bootstrapbread/bootstrapbread.component.css",
    "ts_file_path": "https://ui-gallery.s3.ap-south-1.amazonaws.com/angular/ui-lib/bootstrapbread/bootstrapbread.component.ts",
    "html_file_path": "https://ui-gallery.s3.ap-south-1.amazonaws.com/angular/ui-lib/bootstrapbread/bootstrapbread.component.html",
    "sample_css_file_path": "",
    "sample_ts_file_path": "",
    "sample_html_file_path": "",
    "scripts": "{}",
    "app_image": "https://ui-gallery.s3.ap-south-1.amazonaws.com/images/1646233859-9336133.png",
    "app_name": "bootstrapbread",
    "app_title": "Simple Login page using Bootstrap Form.",
    "app_description": "Simple bootstrap login page design. The theme uses basic Bootstrap forms.",
    "tag": "Login",
    "stack": "angular",
    "type": "angular-ui-lib",
    "created_on": "2022-03-02T15:11:00.242666Z",
    "created_by": 1
}
```


*Make sure the command is executed inside an angular module*

once uploaded successfully, Component can be found at [angular.uigallery.ask-jennie.com](https://angular.uigallery.ask-jennie.com/)

**- Update**

User can also upload their custom made UI module to Jennie for later use.
 
```
jennie angular delete ui-lib
```

*Make sure the command is executed inside an already uploaded angular module, jennie.conf.json should exits in directory*

- ## Version Check
Check software version.
`jennie --version`

**output (logged in user)**
```shell script
Version : A.B.C
Author : ASK Jennie Developer <saurabh@ask-jennie.com>
Stable Version : X.Y.Z
Latest Version : XX.YY.ZZ
The package targets protocol for uploading and reusing task and libraries

User Name : Saurabh Pandey
User Email : saurabh@ask-jennie.com
```

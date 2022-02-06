# Jennie

Jennie is a high-level python automation framework. Jennie provides protocol to upload and reuse automation for different platforms.


## Jennie 0.0.1 release notes
expected release : 2nd week of feb 2022

**The release/0.0.1 contains:**
 
- Working protocol for uploading / updating Angular UI module library.
- Working protocol for reusing Angular UI module library.
- Working protocol for uploading / updating Angular Framework Automations.
- Working protocol for reusing Angular Framework Automations. 
- Working protocol for uploading / updating Django Framework based backend automation.
- Working protocol for reusing Django Framework based backend automation.
- Working custom jennie automation for UBUNTU server ( setup and deploy ) 

## Angular UI module library.

*A list of UI galleries can be found at [angular.uigallery.ask-jennie.com](https://angular.uigallery.ask-jennie.com/)*


## Create Angular UI module library component.
The command creates an angular component and add jennie configration to it by taking some information from user. This saves the time for creating while uploading a new component to jennie library. 

```
$ jennie angular ui-lib create
```

**Output**
```
Name for the UI library component
>> simplebootstraploginpage

Title for the library component
>>  Simple Login page using Bootstrap Form.

Short Description for the library component
>>  Simple bootstrap login page design. The theme uses basic Bootstrap forms.  
```

component with **jennie.conf.json** file is created.
```json
{
    "type": "angular-ui-lib",
    "name": "simplebootstraploginpage",
    "title": "Simple Login page using Bootstrap Form.",
    "description": "Simple bootstrap login page design. The theme uses basic Bootstrap forms.",
    "tag": "[Keyword for the library]",
    "image_file": "[IMAGE_COMPLETE_FILE_PATH]",
    "sample_usage_component": "[COMPONENT_NAME]"
}
```

**jennie.conf.json** explained

key | value |
--- | --- |
type | Defines the type of automation, for angular ui library use angular-ui-lib |
name | Defines the name for the component and should all small with no special characters. the name should be unique within Jennie Angular UI Gallery. |
title | Small title for the component. Same title is displayed at [uigallery.angular](https://uigallery.angular.ask-jennie.com)  |
description | Short description about the ui component the component, the description will be displayed at [uigallery.angular](https://uigallery.angular.ask-jennie.com) |
image_file | image file path showing gallery after being implemented on a component. make sure the path is absolute path. |
sample_usage_component | Component name that contains sample usage for the ui library component.

## Upload Angular UI module library component.
Make sure the command is execute from a ui-component-directory. to create a ui component directory use **Create Angular UI module library component**
```
$ jennie ui-lib angular upload
```
once uploaded successfully, Component can be found at [uigallery.angular](https://uigallery.angular.ask-jennie.com)

## Update Angular UI module library component.
Make sure the command is execute from a ui-component-directory. to create a ui component directory use **Create Angular UI module library component**
```
$ jennie ui-lib angular upload
```
The command updates already created angular ui component. the component must exits at [uigallery.angular](https://uigallery.angular.ask-jennie.com)

## Use Angular UI module library component.
Add a UI component available for public use to your angular project.
```
$ jennie ui-lib angular <ui-gallery-name>
```

the command will create a component with the name of library, add it to project, later the library can be used using 
`<app-uilibname></app-uilibname>` anywhere inside projects

Library with documentation can be found at [uigallery.angular](https://uigallery.angular.ask-jennie.com)

## Angular Framework Automations.

Automation related to angular framework 9+ are stored here.

## Create Angular Framework Automations Directory.
 
```
$ jennie automations angular create
```

The command a directory with 2 files, jennie.conf.json and automation.conf.json

**Output**
```
Name for the UI library component
>> usersessions

Title for the automation
>>  Simple user sessions

Short Description for automation
>>  Create authgaud and session manager which further can use used for creating autentication inside angular project.  
```

component with **jennie.conf.json** file **automation.conf.json** and is created.

- **jennie.conf.json**
```json
{
    "type": "angular-automations",
    "name": "usersessions",
    "title": "Title for the automation",
    "description": "Short Description for automation.",
    "tutorial_file": "path of Tutorial File related to automations"
}
```

- **automation.conf.json**
```json
[
    {
        "type": "raw_files",
        "files": {
            "output_dir": "filepath",
            "output_dir_1": "filepath_1"
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
            "bootstraploginpage", "bootstrapsignuppage", "bootstrapresetpasswordpage"
        ]
    },
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
    },
    {
        "type": "index_css",
        "script": [ "css_path", "css_2_path" ]
    }
]
```

- **automation.conf.json** explained

type | about |
--- | --- |
raw_files | dict of raw files in format "output_path": "filepath". services and other helper scripts can be stored within the key. list of files can be added inside "files". |
shell_command | array of Shell command that is required for automations can be stored here |
ui-lib | User can also store a list of purpose library for automation purpose. [uigallery.angular](https://uigallery.angular.ask-jennie.com)  |
add_routing | the section can include name of component which is created by user to add it to angular routing.
index_script | Files and script required to add in index.html file in angular can be stored in this section |
index_css | Css files that is required for automation can be stored in the section.


## Upload Angular Framework Automations.

Make sure the command is execute from a angular-automation-directory. to create angular-automation-directory use **Create Angular Framework Automations Directory.**
```
$ jennie automations angular upload
```

once uploaded successfully, Automation with description can be found at [automations.angular](https://automations.angular.ask-jennie.com)

## Update Angular Framework Automations.

Make sure the command is execute from a angular-automation-directory

```
$ jennie automations angular update
```

The command updates already created angular automations. the automation must exits at [automations.angular](https://automations.angular.ask-jennie.com)

## Use Angular Framework Automations.

Adds angular based automation to project.

```
$ jennie automations angular <automation-name>
```

Make sure the command is executed from an angular project.

all Automations can be searched at [automations.angular](https://automations.angular.ask-jennie.com).
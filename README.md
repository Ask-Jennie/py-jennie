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

### Create Angular UI module library component.
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

### Upload Angular UI module library component.
Make sure the command is execute from a ui-component-directory. to create a ui component directory use **Create Angular UI module library component**
```
$ jennie angular ui-lib upload
```
once uploaded successfully, Component can be found at [uigallery.angular](https://uigallery.angular.ask-jennie.com)

### Update Angular UI module library component.
Make sure the command is execute from a ui-component-directory. to create a ui component directory use **Create Angular UI module library component**
```
$ jennie angular ui-lib upload
```
The command updates already created angular ui component. the component must exits at [uigallery.angular](https://uigallery.angular.ask-jennie.com)

### Use Angular UI module library component.
Add a UI component available for public use to your angular project.
```
$ jennie angular ui-lib <ui-gallery-name>
```

the command will create a component with the name of library, add it to project, later the library can be used using 
`<app-uilibname></app-uilibname>` anywhere inside projects

Library with documentation can be found at [uigallery.angular](https://uigallery.angular.ask-jennie.com)

## Angular Framework Automations.

### Create Angular Framework Automations.

### Upload Angular Framework Automations.

### Update Angular Framework Automations.

### Use Angular Framework Automations.

## Django Framework based backend automation.

### Create Angular Framework Automations.

### Upload Angular Framework Automations.

### Update Angular Framework Automations.

### Use Angular Framework Automations.

## Automation for UBUNTU server ( setup and deploy )
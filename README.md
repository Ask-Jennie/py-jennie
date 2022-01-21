# Ask Jennie Python Package
The package targets to automate development task using single line command, The package include task with UI gallery to automate development of small to medium project. The package is a part of ASK Jennie Complete Product.

## Setup

```shell script
jennie setup useremail@something.com 
```

To use to library user needs to get them registered with ASK Jennie, to request registration
Mail us on : saurabh@ask-jennie.com

Registered user can simply do setup and start using Jennie.

## Angular Based Automations
- ### Installing Bootstrap in Angular Project
```shell script
jennie angular install bootstrap
```

*Adds Bootsrap and Jquery to angular project*

## Adding Angular Based UI Component
```shell
jennie angular add ui-lib-name
```
replace `ui-lib-name` with desire gallery, a list of UI galleries can be found at [gallery.angular.ask-jennie.com](https://gallery.angular.ask-jennie.com)


## Uploading Angular Based UI Component
Steps to upload a UI component to Jennie.

- Create a json config file inside the component folder, the json config file will contain
```json
{
    "type": "bootstrap-ui-gallery",
    "name": "register",
    "title": "Simple Bootstrap Registration Page",
    "description": "Some imformation about the library",
    "image_file": "/Users/saurabhpandey/Downloads/navbar-light.png"
}
```
`type`: `bootstrap-ui-gallery` / `ui-gallery`

`name`: `nameofcomponent`, make sure the name should not contain only alpha numaric characters.

`title`: Title for the component, the title will be displayed on ui gallery website.

`description`: Short description for the component, the description will be displayed on ui gallery website.

`image_file`: File path for image, required. Make you component live take a screenshot that's good for an image.

- Open Terminal and go project/src/app/path/to/component 
![GoToTerminal](images/go_to_project_component.png)

- execute
```shell
jennie angular upload bootstrap-ui-lib
```


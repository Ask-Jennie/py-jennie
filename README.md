# Jennie Python Package
Jennie is a collection of automation on different framework. To use the one must be registered with Ask Jennie. [Register Here](https://dashboard.ask-jennie.com)

## Install ASK Jennie
ASK Jennie library is available on PIP for public use. to install jennie 
```shell script
pip3 install py-jennie
```
Once installation is completed, use below command to setup jennie for the first time.
```shell script
jennie setup useremail@something.com 
```

## About PY Jennie
Jennie is a collection of automation on different software framework. These automation can be used by developers in order to increase productivity.

Currently library supports automation for below frameworks  

###  Angular ( Frontend )

Automation related to Angular 7+ framework. The base command 

```shell script
jennie angular [TASK_TYPE] [TASK_NAME]
```

The list of features available are

#####-  Installing Bootstrap in Angular Project

Adds Bootstrap and Jquery to angular project. 

```shell script
jennie angular install bootstrap
```
        
*One need to be present inside angular project to perform the task.*

##### -  Installing Angular Material in Angular Project

Adds Angular material To a project. 

```shell script
jennie angular install angular-matarial
```
        
*One need to be present inside angular project to perform the task.*

##### - Adding Dashboard Theme to a project

Dashboard theme : The flow include signup page, login page, dashboard module and inside dashboard module home and other pages.

Also the flow includes AuthGaurd for managing authenticated pages.


```shell script
jennie angular add dashboard-theme
```

##### -  Adding User Session Flow

Adds User session with auth manager, which can be used to hide unauthenticated user from accessing any page
Adds AuthGaurd Services, UserSession Services and dummy login api to a project.

```shell script
jennie angular add user-session
```
 
*One need to be present inside angular project to perform the task.*
   
##### -  Adding Firebase

Firebase is a great tool for automating backend services though due to multiple steps involved it becomes hard to integrate firebase in Angular Project. 

The command adds Handler for Firebase that makes integrations and firebase usage easy to use inside project

```shell script
jennie angular add firebase
```
 
*One need to be present inside angular project to perform the task.*

##### -  Add Table View For API

Add a page with table that represent value from API, also there are option to add, modify and delete value.

```shell script
jennie angular add table-view path/to/table.json
```
 
*One need to be present inside angular project to perform the task.*
      
#### Django ( Backend )

##### -  Setup Project

The command and configure application to Django Project with proper directory structure and with custom libraries.

Custom libraries include

- LogginMixin : Simple Django Logger with option to log to ElasticSearch
- Authentication : Token Authentication class with permission class.
- CustomExceptionHandler : for handling real time exceptions
- CustomResponse : The helps to maintain proper structure standard for API response. 

```shell script
jennie django setup project
```

##### -  Create User API

The task automates creation of 

- Login API
- Signup API
- Reset Password API

```shell script
jennie django add user-apis path/to/user-table.json
```

##### -  Create Simple API

The task automates create Api for a table provided. The api contain all 4 methods. GET, POST, PUT, DELETE.

Create Model, Serializer, Controller, and View for the API.
 
```shell script
jennie django add simple-apis path/to/user-table.json
```

### Angular Bootstrap UI Gallery

`Angular component library`: Angular Library that can be used inside any angular project as a component, these component can be a small module or a complete page as well.

*A list of UI galleries can be found at [angular.uigallery.ask-jennie.com](https://angular.uigallery.ask-jennie.com/)*

##### - Adding Angular Based UI Component

```shell
jennie angular add uilibname
```
        
replace `uilibname` with desire gallery        
        
**the command will create a component with the name of library, add it to project, later the library can be used using `<app-uilibname></app-uilibname>` anywhere inside projects**

#####-  Uploading Angular Based UI Component
Steps to upload a UI component to Jennie.

- Create a json config file inside the component folder, the json config file will contain
```json
{
    "type": "bootstrap-ui-gallery",
    "name": "navbardark",
    "title": "Simple Bootstrap Registration Page",
    "description": "Some information about the library",
    "parameter": [{
        "parameter_name": "Name of parameter",
        "parameter_type": "string/array",
        "parameter_description": "Tell us about the parameter"
    }],
    "image_file": "/Users/saurabhpandey/Desktop/ASKJennie/uigallery/src/assets/navbar-dark.png",
    "tag": "Navbar"
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
jennie angular upload ui-lib
```

#### - Flutter ( Mobile Application, Coming Soon.... ) 

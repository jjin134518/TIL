# Django for Dummies



## 1. How to start a django project

❗start from a folder that you want to create your project

❗It is a good idea to make a one big storage folder that will have several Django projects inside for organization

🎯 Example: make 02_model folder with project named Model1 and app named orm_practice

<hr> </hr>

#### < Start from bash terminal >

| Process                                                      | Commends                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| create **project root** folder(02_MODEL). <br>**Move in** to the created directory   <br> **use all cap to distinguish it from regular folders. | ``` mkdir 02_MODEL``` <br>```cd 02_MODEL```                  |
| **Create** virtual environment & **activate**                | ``` python -m venv venv ```<br>```source venv/Script/activate```<br> |
| **check** virtual environment<br>must be within the folder you made not in global | ``` which python ```                                         |
| **Install** necessary programs                               | ```pip install django django_extensions ipython```           |
| **Create** django **project**<br />include '.' to unzip and make it directly in the folder | ```django-admin startproject <project name> .```             |
| **Open** project in vscode                                   | ```code .```                                                 |
| Extra Codes**<br />delete project (only one project started)<br />update pip (get rid of warning) | `rm -rf manage.py model`<br />`python -m install --upgrade pip` |

#### < In VSCode >

| Process                                                     | Code                                                         |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| **Preset** venv environment & **check**                     | `ctrl + shft + p / select interpreter / (venv/Scripts/python)`<br />`python 3.x.x 64-bit('venv')` |
| **Create** an app                                           | `python manage.py startapp orm_practice`                     |
| **Add** django_extentions in project folder **settings.py** | `line 33 'django_extensions'`                                |
| **Update** settings.py when create apps                     | `line 33 'yourappname'`                                      |


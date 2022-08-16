## Project Installation

* Note this project has a .env file with the secret key


The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Lilywd/Django-Authentication.git
$ cd Django-Authentication
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -3 -m venv .venv
$ .venv\Scripts\activate.bat
$ code .
$ .venv\Scripts\Activate.ps1
```



Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment .

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ cd Backend
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.



## Project Features
* User authentication and authorization
* User tracking and history
* Responsive contact us form
* Google sign-in authorization
* User profile with change  profile image ,email and password
* Forgot passoword and Reset
* Qrcode generation and download (png,jpeg,pdf)
* Share  to social media accounts
* 






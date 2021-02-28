# Event Manger
---
## Stack
---
This project has been built using Django 3, and Python 3.

For more details on dependencies, please check [requirements.txt](https://github.com/tmczqq/sda-event-manager/blob/main/requirements.txt).

## Getting Started
---
### Install Git
First, make sure you have [Git](https://git-scm.com/downloads) already installed.

It usually comes pre-installed in Mac and Linux but in Windows you need to run the installer available in the link above.

### Install virtualenv
Also make sure you have [virtualenv](https://virtualenv.pypa.io/en/latest/installation/) in your computer by running:

```
virtualenv --version
```
If you get an error, use pip (included in Python3) with the following command:

```
pip install virtualenv
```

### Configure your local repository
If you haven't already, fork the project at https://github.com/tmczqq/sda-event-manager

Clone your forked repository in your computer (see detailed instructions [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

Navigate to the repository's location using the command line: cd EventManager

Add https://github.com/tmczqq/sda-event-manager.git to remote following these [instructions](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)

### Configure the virtual environment
If you have Python3 already configured as the default version for your computer, just run:
`virtualenv ./env`

### Install dependecies and migrate the database
If you are in Mac or Linux:
```
./env/bin/pip install -r requirements.txt
```
```
./env/bin/python manage.py migrate
```
If you are in Windows:
```
pip install -r requirements.txt
```
```
python manage.py migrate
```

### Rename the local_settings file
Find the file `local_settings.example` and copy it in `local_settings.py` with the following command:

```
cp local_settings.example local_settings.py
```

### Create a super user
If you're in Mac or Linux run:
```
./env/bin/python manage.py createsuperuser
```
If you are in Windows:
```
python manage.py createsuperuser
```

### Start the server
If you're in Mac or Linux run:
```
./env/bin/python manage.py runserver
```
If you're in Windows:
```
python manage.py runserver
```



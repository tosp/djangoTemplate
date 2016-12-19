# djangoTemplate
How to use the template

[![Build Status](https://travis-ci.org/tosp/tospHome.svg?branch=master)](https://travis-ci.org/tosp/tospHome)

## System Requirements

* [Python 3.5](https://www.python.org/downloads/)
* [PostgreSQL 9.5+](https://wiki.postgresql.org/wiki/Detailed_installation_guides)
* [Node 4+](https://docs.npmjs.com/getting-started/installing-node)

## Virtual Environments

You will need to create a virtual environment in order to isolate all the packages that are required for the project. We provide instructions on how to do it with [`virtualenv`](https://virtualenv.pypa.io/en/stable/)

First find the path to your `python 3.5` installation by running

```bash
$ which python3.5
PATH TO PYTHON 3.5
```

Then create the virtual environment like this. (We use different virtualenvironments for different functions, such as testing, development, production, and CI, each of them has different requirements, you should at least create an environment for development and one for testing.)
```bash
$ virtualenv --python='PATH TO PYTHON 3.5' /path/to/your/venv/NAME_OF_YOUR_ENV
```

We use environment variables to separate sensitive information and keys from the code, you should set the following ones.

```bash
DJANGO_SETTINGS_MODULE='tospHome.settings.development' //The last part depends on the environment you are on
SECRET_KEY='Generate one here. (http://www.miniwebtool.com/django-secret-key-generator/)'
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

In order to set them in your virtualenv just go to `/path/to/your/venv/NAME_OF_YOUR_ENV/bin/activate` and in the section for deactivate add at the end

```bash
unset NAME_OF_ENV_VAR
```
And set the variable at the end of the file like this

```bash
export NAME_OF_ENV_VAR='VALUE OF VAR'
```

After you are finished you can activate your virtual environment by running
```bash
$ source /path/to/your/venv/NAME_OF_YOUR_ENV/bin/activate
```

And deactivate it just by running this command on the terminal
```bash
$ deactivate
```

## Installing the Project Requirements

You will need to install different packages depending on the environment you are working on. For example if you are setting up the `development` environment you will need to run

```bash
$ pip install -r requirements/development.txt
```
Then install the npm required with
```bash
$ npm install
```

## Running the project

Once you have finished the setup, you can run the project.

```bash
Run the migrations
$ python manage.py migrate
Start the development server
$ python manage.py runserver
```
After this you can go to your browser and go to http://localhost:8000, and you should be able to see the project running.

# Thank you!!!

All your contributions are highly appreciated. You are awesome and we hope you have a great day.
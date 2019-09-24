# renv

created a pip env (virtual environment)
use . ./Scripts/activate

download django, rest_framework
pip install django, rest_framework

create a database in mysql = recruitmentdb

setting.py

INSTALLED_APPS = [
    'rest_framework',
    'restapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recruitmentdb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',

    }
}


import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEB_H_NAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEB_HOST_NAME']]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhitenoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT =   os.path.join(BASE_DIR, 'staticfiles')

connection_string = os.environ['AZURE_MYSQL_CONNECTIONSTRING']
parameters = {pair.split('='):pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': parameters['dbname'],
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
        'HOST': parameters['host']
    }
}
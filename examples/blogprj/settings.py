# -*- coding: utf-8 -*-

import platform
import sys
import os

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_ROOT, '../../../'))
from mongoengine import connect

connect('mongoforms_test')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

sys.path.append(os.path.join(PROJECT_ROOT, '../../'))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media')
TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, 'templates')]
ADMIN_MEDIA_PREFIX = '/media/'
ROOT_URLCONF = 'blogprj.urls'
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

INSTALLED_APPS = (
    'apps.blog',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.core.context_processors.auth",
    "django.core.context_processors.media",
    "django.core.context_processors.debug",
)

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)


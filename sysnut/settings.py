# -*- coding: utf-8 -*-
"""
Django settings for sysnut project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.contrib.messages import constants as messages
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f^-7=a3d2irfx0ey5d$5rceq1t-t884cw=4l!$!%c@tzi%ry**'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
COMPRESS_ENABLED = True
SITE_ID = 1
ALLOWED_HOSTS = ['*']

LANGUAGES = [
    ('pt-br', _('Portuguese')),
    ('en', _('English')),
    ('es', _('Spanish')),
]
LANGUAGE_CODE = 'pt-BR'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/')
]

# Application definition

INSTALLED_APPS = [
    #App autocomplete
    'dal',
    'dal_select2',
    #Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #Other apps
    'sass_processor',
    "compressor",
    'widget_tweaks',
    'xlrd',
    'multiupload',
    'django_messages',
    #My apps
    'sysnut.core',
    'sysnut.account',
    'sysnut.nutritionist',
    'sysnut.patient',
    'sysnut.food',
]

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'sysnut/sysnut/core/static/css'),
    #os.path.join(BASE_DIR, 'sysnut/core/node_modules'),
]

SASS_PROCESSOR_AUTO_INCLUDE = False
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
]

SASS_PRECISION = 8
SASS_OUTPUT_STYPE = 'compact'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # Internationalization
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'sysnut.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django_messages.context_processors.inbox',
                'django.template.context_processors.i18n',
            ],
        },
    }
,]

WSGI_APPLICATION = 'sysnut.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/


TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'sysnut/core/static')
#print(STATIC_ROOT)
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")


#MEDIA files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Auth
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'core:instructions'
LOGOUT_URL = '/accounts/logout'

# MESSAGE DJANGO
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


#SETTINGS LOCAL
try:
    exec(open(os.path.join(BASE_DIR,'bankhours/settings_local.py')).read())
except IOError as e:
    pass

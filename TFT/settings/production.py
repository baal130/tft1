"""
Django settings for testzs project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import dj_database_url
from decouple import Csv, config
from unipath import Path
from django.utils.translation import ugettext_lazy as _
from django.contrib.messages import constants as messages


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  # BASE_DIR =     os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_9sfr9be0ogbt7jz!5k9euc19af0gzt_0^bp$!xgcyzcv6&ws+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','tft1.herokuapp.com',  'https://tft1.herokuapp.com']
SERVICE_LIST = []

# Application definition
EMAIL_HOST='mail.idc.hr'
EMAIL_HOST_USER='shop@idc.hr'
EMAIL_HOST_PASSWORD=os.environ.get("EMAIL_HOST_PASSWORD",'none')

EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL ='shop@idc.hr'

INSTALLED_APPS = (
    'modeltranslation', #https://django-modeltranslation.readthedocs.io/en/latest/registration.html
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects', #for 301 redirects 
   
    'constrainedfilefield',
    'crispy_forms',
    'bootstrap_datepicker_plus',
    'bootstrap3',
    
    #my_aps
    'Students',
    
    #social apps/auth
    'allauth',
    'allauth.account',
    
    # 'authentication',
)

MIDDLEWARE = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',#for 301 redirectspy




)
ROBOTS_USE_SCHEME_IN_HOST = True

# for HTTPS AND REDIRECTS TO HTTPS://www.
CORS_REPLACE_HTTPS_REFERER      = True
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True

ROOT_URLCONF = 'TFT.urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),
           os.path.join(BASE_DIR, "templates/landing"),
            ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                
            ],


            
        },
    },
]

WSGI_APPLICATION = 'TFT.wsgi.application'
AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
    }
}
# 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
CACHES = {
'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            }
}
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'hr-ru'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = [
   
    ('hr', _('Hrvatski')),
]

DATE_INPUT_FORMATS=[
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
    '%d/%m/%y',              # '10/25/06'
    
]
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True
# if this is true gogle map will not work longiture is receveid like 1,5 instead 1.5 , can be resloved with localization off tag
USE_TZ = True

#Crispy FORM TAGs SETTINGs
CRISPY_TEMPLATE_PACK ='bootstrap3'
BOOTSTRAP3 = {
    'include_jquery': True,
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "Static_in_venv","static_root")# copied from staticfiles(our static) dirs u invirormnt directory(izvan roota)

STATICFILES_DIRS = (                    #staticne filovi u projektu gdje se nalaze kopiraju se u static root koji se koristi
    os.path.join(BASE_DIR, "Static_in_pro","our_static"),
    # '/var/www/static/',
    #os.path.join(os.path.dirname(BASE_DIR), "Static_in_env"),
) 

MEDIA_URL= '/media/'
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR), "Static_in_venv","media_root")

CACHES = {
'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            }
}

SESSION_SAVE_EVERY_REQUEST=False
SITE_ID=2
LOGIN_REDIRECT_URL ='/'
# LOGIN_REDIRECT_URL ='/'
#Specifies the login method to use – whether the user logs in
 #by entering their username, e-mail address, 
#or either one of both. Setting this to “email” requires ACCOUNT_EMAIL_REQUIRED=True
##FOR ALLAUTH
ACCOUNT_AUTHENTICATION_METHOD ="username_email"
ACCOUNT_USERNAME_REQUIRED = True
# ACCOUNT_USER_MODEL_USERNAME_FIELD="email"
ACCOUNT_EMAIL_REQUIRED= True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_CONFIRMATION = "mandatory"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_ON_EMAIL_CONFIRMATION = True
DEFAULT_HTTP_PROTOCOL = "http" #url is created in allauth adapter.py line 97 need to be html template not txt



AWS_ACCESS_KEY_ID = "AKIAWDFTQUMH57RFOZNM"
AWS_SECRET_ACCESS_KEY =os.environ.get("AWS_SECRET_ACCESS_KEY ",'none')

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'TFT.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'TFT.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'tft1'
S3DIRECT_REGION = 'eu-central-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


AWS_IS_GZIPPED =True

import datetime

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_S3_OBJECT_PARAMETERS = { 
    'Expires': expires,
    'CacheControl': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
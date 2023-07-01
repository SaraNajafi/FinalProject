from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6xq1m#!o1pt-l8==&ho#3o8080&#%y-wc*+9yu2l(%!!mb5hi='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['saranajafi.net', 'www.saranajafi.net']


#site framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {  
#         'ENGINE': 'django.db.backends.mysql',  
#         'NAME': 'saranaja_mydatabase',  
#         'USER': 'saranaja_sara',  
#         'PASSWORD': 'Khakhs7394!',  
#         'HOST': 'localhost',  
#         'PORT': '3306',  
#     }  
# }

STATIC_ROOT=BASE_DIR / 'static'
MEDIA_ROOT=BASE_DIR / 'media'

STATICFILES_DIRS =[
    BASE_DIR / "statics"
]

CSRF_COOKIE_SECURE = False  # or False for development
CSRF_COOKIE_HTTPONLY = True

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_USE_SESSIONS = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

#CSRF_COOKIE_SECURE = True
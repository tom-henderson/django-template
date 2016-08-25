"""Common settings and globals."""
import os

#  PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
CONFIG_ROOT = os.path.dirname(os.path.dirname(__file__))
DJANGO_ROOT = os.path.dirname(CONFIG_ROOT)

PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)

SITE_NAME = os.path.basename(DJANGO_ROOT)

# SECRET CONFIGURATION
# Note: This key should only be used for development and testing.
SECRET_KEY = "{{ secret_key }}"

# DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

# MANAGER CONFIGURATION
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

# GENERAL CONFIGURATION
TIME_ZONE = 'Pacific/Auckland'
USE_TZ = True

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

SITE_ID = 1
WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)

# URL CONFIGURATION
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# MEDIA CONFIGURATION
MEDIA_ROOT = os.path.join(DJANGO_ROOT, 'media')
MEDIA_URL = '/media/'

# STATIC FILE CONFIGURATION
STATIC_ROOT = os.path.join(DJANGO_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(CONFIG_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            DJANGO_ROOT,
            'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = ()

LOCAL_APPS = (
    'common',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

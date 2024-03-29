"""Common settings and globals."""
import os

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting, default=None):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        if default:
            return default
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


#  PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
CONFIG_ROOT = os.path.dirname(os.path.dirname(__file__))
DJANGO_ROOT = os.path.dirname(CONFIG_ROOT)
PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)

SITE_NAME = os.path.basename(CONFIG_ROOT)

# SECRET CONFIGURATION
# Note: This key should only be used for development and testing.
SECRET_KEY = "{{ secret_key }}"

# DEBUG CONFIGURATION
DEBUG = False
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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

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
    'npm.finders.NpmFinder',
)

# TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(DJANGO_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# MIDDLEWARE CONFIGURATION
MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# APP CONFIGURATION
# Whitenoise must go here too so it loads before django.contrib.staticfiles
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    # 'taggit',
    # 'taggit_helpers',
    # 'rest_framework',
    # 'taggit_serializer',
)

LOCAL_APPS = ()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Django NPM
NPM_ROOT_PATH = PROJECT_ROOT
NPM_STATIC_FILES_PREFIX = 'npm'
NPM_FILE_PATTERNS = {
    'bootstrap': [
        'dist/css/*.min.*',
        'dist/fonts/*',
        'dist/js/*.min.*',
    ],
    'font-awesome': [
        'css/*.min.*',
        'fonts/*',
    ],
    'jquery': [
        'dist/jquery.min.js',
    ],
}

from WeighIn.settings_prod import *

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangotoolbox',
    'rest_framework',
    'api_v1',
    'rest_framework_swagger',
)

ALLOWED_HOSTS = ['api.weighin.me']

ROOT_URLCONF = 'WeighIn.urls_api'

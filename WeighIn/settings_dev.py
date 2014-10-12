from WeighIn.settings import *

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'weighin_dev',
#       'USER': 'admin',
#       'PASSWORD': 'password',
        'HOST': 'dbs.weighin.me',
        'PORT': 8080,
    }
}

ALLOWED_HOSTS = ['dev.weighin.me']

SECRET_KEY = '$c)vj1w(jat5stxjuc2gii%qdbpa%r!358s)a#sewl#zr_ugqn'

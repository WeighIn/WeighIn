from WeighIn.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'weighin',
        'HOST': 'dbs.weighin.me',
        'PORT': 8080,
    }
}

ALLOWED_HOSTS = ['weighin.me']

SECRET_KEY = '$c)vj1w(jat5stxjuc2gii%qdbpa%r!358s)a#sewl#zr_ugqn'

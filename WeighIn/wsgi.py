"""
WSGI config for WeighIn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

build_env_default = 'dev'
build_env_settings = {
    'dev': 'WeighIn.settings_dev',
    'prod': 'WeighIn.settings_prod',
    'prod_api': 'WeighIn.settings_prod_api',
    'prod_web': 'WeighIn.settings_prod_web',
}

import os

settings = build_env_settings.get(os.environ.get('BUILD_ENV', build_env_default).lower())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())

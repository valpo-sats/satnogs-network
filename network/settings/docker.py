import os
from base import *  # flake8: noqa

ENVIRONMENT = 'dev'

# Debug
DEBUG = True

# Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cache
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://redis:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        },
        'KEY_PREFIX': 'network-{0}'.format(ENVIRONMENT)
    }
}

ALLOWED_HOSTS = [
    os.getenv('ALLOWED_HOSTS', '*')
]

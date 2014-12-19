import os
from base import *


# Apps
INSTALLED_APPS = Common.INSTALLED_APPS
INSTALLED_APPS += ('djangosecure', )

# Security
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*')

# Templates
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# Analytics
GOOGLE_ANALYTICS_PROPERTY_ID = os.getenv('DJANGO_GOOGLE_ANALYTICS_PROPERTY_ID', False)
GOOGLE_ANALYTICS_DOMAIN = os.getenv('DJANGO_GOOGLE_ANALYTICS_DOMAIN', False)

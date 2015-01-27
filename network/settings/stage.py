import os
from base import *

# Security
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*')

# Mail
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = os.getenv('DJANGO_DEFAULT_FROM_EMAIL', 'noreply@example.com')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

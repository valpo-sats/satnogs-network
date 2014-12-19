#!/usr/bin/env python
import dotenv
import django.core.handlers.wsgi

dotenv.read_dotenv()
application = django.core.handlers.wsgi.WSGIHandler()

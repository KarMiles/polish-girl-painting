"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
from django.core.wsgi import get_wsgi_application

"""
WSGI config for pgp_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pgp_project.settings')
application = get_wsgi_application()

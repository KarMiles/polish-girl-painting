"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
from django.core.asgi import get_asgi_application


# ASGI config for pgp_project project.
# It exposes the ASGI callable as a module-level variable named ``application``.
# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pgp_project.settings')
application = get_asgi_application()

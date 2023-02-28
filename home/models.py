"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


class HomeSettings(models.Model):
    """
    Contains settings for the webpage
    controllable by user
    """
    class Meta:
        verbose_name_plural = 'Settings'

    background_image = models.ImageField(
        null=True,
        blank=True)

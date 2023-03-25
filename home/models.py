"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


class HomeSettings(models.Model):
    """
    Contains settings for the home page
    controllable by authorized user
    """
    class Meta:
        """
        Set expression to display for Home Settings on admin page.
        Owner can change background image in this section.
        """
        verbose_name_plural = 'Settings'

    background_image = models.ImageField(
        null=True,
        blank=True)

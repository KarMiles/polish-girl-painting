"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.contrib.auth.models import User


# Models for contact app


class Contact(models.Model):
    """
    A class for the contact model
    """
    name = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="contact",
        null=True,
        blank=True)
    contact_name = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default="")
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False)
    subject = models.CharField(
        max_length=255)
    body = models.TextField(
        max_length=3000)
    created_on = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        """
        Set expression to display for contact settings on admin page
        """
        verbose_name_plural = 'Messages'

    def __str__(self):
        """
        Returns the message body string
        Args:
            self (object): self.
        Returns:
            The message body string
        """
        return format(self.subject)

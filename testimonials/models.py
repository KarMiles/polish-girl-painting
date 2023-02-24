"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib.auth.models import User


# Field choices

# Priority
PRIORITY_CHOICES = [
    ("1 - Top", "Top"),
    ("2 - High", "High"),
    ("3 - Normal", "Normal"),
    ("4 - Low", "Low"),
    ("5 - Lowest", "Lowest"),
]


# Models for testimonials app

class Testimonial(models.Model):
    """
    Class for the Testimonial model
    representing a testimonial written by user
    """
    class Meta:
        """
        Order posts by creation time
        """
        ordering = ['live', 'priority', '-created_on']

    def __str__(self):
        """
        Returns the testimonial content string
        Args:
            self (object): self.
        Returns:
            The testimonial content string
        """
        return self.content

    title = models.CharField(
        max_length=150,
        null=True,
        blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="testimonials",
        null=True,
        blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="3 - Normal",
        null=True,
        blank=True)
    about_me = models.BooleanField(
        default=False)
    live = models.BooleanField(
        default=False)

"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib.auth.models import User


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
        ordering = ['-created_on']

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
        on_delete=models.CASCADE,
        related_name="testimonials")
    content = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)
    live = models.BooleanField(
        default=False)

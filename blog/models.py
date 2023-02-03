"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib.auth.models import User


# Models for blog app

class Post(models.Model):
    """
    Class for the Post model
    representing a description of a treatment
    """
    title = models.CharField(
        max_length=150,
        unique=True)
    slug = models.SlugField(
        max_length=150,
        unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts")
    content = models.TextField()
    featured_image = models.ImageField(
        null=True,
        blank=True)
    highlight = models.BooleanField(
        default=False)
    live = models.BooleanField(
        default=True)
    created_on = models.DateTimeField(
        auto_now_add=True)
    updated_on = models.DateTimeField(
        auto_now=True)

    class Meta:
        """
        Order posts by creation time
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Returns the post title string
        Args:
            self (object): self.
        Returns:
            The post title string
        """
        return format(self.title)

"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Post


# Models for blog management in admin page

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin class for the blog model.
    Section for managing posts.
    """
    list_display = (
        'title',
        'live',
        'highlight',
        'created_on',
        'updated_on')
    search_fields = [
        'title',
        'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = (
        'live',
        'highlight')

# Decoration replaces class:
# admin.site.register(Post)

"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Post, BlogSettings


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
    summernote_fields = ('content',)
    list_filter = (
        'live',
        'highlight')

    actions = ['make_live', 'make_not_live']

    def make_live(self, _request, queryset):
        """
        Change status of a post to live (live True)
        """
        queryset.update(live=True)

    def make_not_live(self, _request, queryset):
        """
        Change status of a post to live (live True)
        """
        queryset.update(live=False)


@admin.register(BlogSettings)
class SettingsAdmin(admin.ModelAdmin):
    """
    Admin class for managing blog settings.
    When 'live' blog is active and posts are visible,
    otherwise all posts are hidden.
    """
    list_display = (
        'live',)

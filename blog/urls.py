"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.urls import path

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from . import views


# URL patterns for the app blog

urlpatterns = [
    path(
        "",
        views.PostList.as_view(),
        name="blog"),
    path(
        "post",
        views.CreatePost.as_view(),
        name="post_create"),
    path(
        "<slug:slug>/",
        views.PostDetail.as_view(),
        name="post_detail"),
    path(
        "delete/<slug:slug>/",
        views.DeletePost.as_view(),
        name="post_delete"),
    path(
        "edit/<slug:slug>/",
        views.EditPost.as_view(),
        name="post_edit"),
]
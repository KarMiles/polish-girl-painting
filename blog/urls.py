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
        views.post_list,
        name="blog"),
    path(
        "post",
        views.CreatePost.as_view(),
        name="post_add"),
    path(
        "<slug:slug>/",
        views.PostDetail.as_view(),
        name="post_detail"),
    path(
        "post_edit/<slug:slug>/",
        views.EditPost.as_view(),
        name="post_edit"),
    path(
        "post_delete/<slug:slug>/",
        views.DeletePost.as_view(),
        name="post_delete"),
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path(
        "",
        views.Index.as_view(),
        name="home"),
]

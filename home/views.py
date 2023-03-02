"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import Post
from .models import HomeSettings


def index(request):
    """ A view to return the index page"""
    template = 'home/index.html'

    latest_settings = HomeSettings.objects.order_by('-id').first()
    image = latest_settings

    posts = Post.objects.filter(highlight=True).filter(live=True)
    context = {
        'background_image': image,
        'posts': posts,
    }

    return render(request, template, context)

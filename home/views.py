"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
# from django.views import generic
from django.shortcuts import get_object_or_404

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


# def index(request):
#     """ A view to return the index page"""
#     return render(request, 'home/index.html')

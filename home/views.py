"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from django.views import generic, View

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from blog.models import Post


# def index(request):
#     """ A view to return the index page"""
#     return render(request, 'home/index.html')


class Index(generic.ListView):
    """ A view to return the index page"""
    model = Post
    posts = Post.objects.all()
    template_name = "home/index.html"
    ordering = ['-created_on']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(highlight=True).filter(live=True)

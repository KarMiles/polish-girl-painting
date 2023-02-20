"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from products.models import Category


def index(request):
    """ A view to return the index page"""
    return render(request, 'home/index.html')


# def index(request):
#     """ A view to return the index page"""
#     categories = Category.objects.all()

#     context = {
#         'categories': categories,
#     }

#     return render(request, 'home/index.html', context)

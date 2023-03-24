"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render
from django.contrib.auth.mixins import AccessMixin

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Views for error pages

def handler403(request):
    """
    View to render 403 error page is called for unauthorized user.
    Args:
        request (object): HTTP request object
        exception: exception error
    Returns:
        Render 403 error page
    """
    return render(
        request,
        'errors/403.html',
        status=403)


def handler404(request):
    """
    View to render 404 error page when non-existent page is called.
    Args:
        request (object): HTTP request object
        exception: exception error
    Returns:
        Render 404 error page
    """
    return render(
        request,
        'errors/404.html',
        status=404)


def handler500(request):
    """
    View to render 500 error page in case of server error
    Args:
        request (object): HTTP request object
    Returns:
        Render 500 error page
    """
    return render(
        request,
        'errors/500.html',
        status=500)


# Views for testing error pages

def test_403_view(request):
    """
    View to render 404 error page when non-existent page is called.
    Args:
        request (object): HTTP request object
        exception: exception error
    Returns:
        Render 403 error page
    """
    return render(
        request,
        'errors/403.html')


def test_404_view(request):
    """
    View to render 404 error page when non-existent page is called.
    Args:
        request (object): HTTP request object
        exception: exception error
    Returns:
        Render 404 error page
    """
    return render(
        request,
        'errors/404.html')


def test_500_view(request):
    """
    View to raise Exception
    for manual testing 500 error page
    Args:
        request (object): HTTP request object
    Returns:
        Render 500 error page
    """
    # Return an "Internal Server Error" 500 response code.
    # raise Exception('test')
    return render(
        request,
        'errors/500.html')


# Access management

class StaffRequiredMixin(AccessMixin):
    """
    Verify that the current user
    is authenticated as member of staff.
    """
    def dispatch(self, request, *args, **kwargs):
        """
        Grant access only to staff users.
        """
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

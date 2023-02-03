"""Imports"""
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.contrib import messages

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from accounts.views import StaffRequiredMixin
from .models import Post
from .forms import PostForm


# Views for blog app

class CreatePost(generic.CreateView):
    """
    A view to create a post
    Args:
        CreateView: class based view
    Returns:
        Render of post form with success message and context
    """
    template_name = "blog/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        """
        Set post author and slug to self instances
        Send confirmation message
        Args:
            self (object): self.
            form (object): form.
        Returns:
            The form
        """
        def __init__(self, form):
            self.object = form.instance

        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)

        response = super().form_valid(form)
        messages.add_message(
            self.request,
            messages.INFO,
            'Post created successfully!')
        return response

    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])


class EditPost(StaffRequiredMixin, generic.UpdateView):
    """
    A view to edit a post
    Args:
        StaffRequiredMixin
        UpdateView: class based view
    Returns:
        Render of updated post with success message
    """
    template_name = "blog/post_create.html"
    form_class = PostForm
    queryset = Post.objects.all()

    def form_valid(self, form):
        """
        Set post author and slug to self instances
        Send confirmation message
        Args:
            self (object): self.
            form (object): form.
        Returns:
            The form
        """
        def __init__(self, form):
            self.object = form.instance
            self.object.author = self.request.user
            self.object.slug = slugify(self.object.title)

        messages.add_message(
            self.request,
            messages.INFO,
            'Post submitted successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])


class DeletePost(StaffRequiredMixin, generic.DeleteView):
    """
    A view to delete a post
    Args:
        StaffRequiredMixin
        DeleteView: generic class based view
    Returns:
        Request confirmation of post deletion
        Redirect home after delete
    """
    success_url = reverse_lazy('blog_home')
    queryset = Post.objects.all()
    template_name = 'blog/post_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object,
        then redirect to the success URL
        and show confirmation message.
        """
        self.object = self.get_object()  \
            # pylint: disable=attribute-defined-outside-init

        success_url = self.get_success_url()
        self.object.delete()

        messages.add_message(
            self.request,
            messages.INFO,
            'Post deleted successfully!')

        return HttpResponseRedirect(success_url)


class PostList(generic.ListView):
    """
    A view to show posts
    Args:
        UpdateView: class based view
    Returns:
        Render main page with paginated list of posts
        Posts ordered by priority
        Non-staff users see live posts only
        Staff users see live and draft posts
    """
    model = Post
    template_name = "blog/blog.html"
    # paginate_by = 3
    ordering = 'created_on'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(live=True)


class PostDetail(View):
    """
    A view to show posts
    Args:
        View: class based view
    Returns:
        Render post details
    """
    def get(self, request, slug):
        """
        Get post
        Args:
            self (object): self.
            request (object): HTTP request object.
            slug: slug
        Returns:
            Render post details page with context.
        """
        queryset = self.get_queryset()
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
            },
        )

    def get_queryset(self):
        """
        Filters the post by the query
        Args:
            self (object): Self object
        Returns:
            List of posts Live or Draft for staff,
            only Live for non-staff users,
            order posts by creation time.
        """
        if self.request.user.is_staff:
            return Post.objects.order_by("crated_on")

        return Post.objects.filter(live=True).order_by("created_on")

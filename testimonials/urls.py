from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.all_testimonials,
        name='testimonials'),
    path(
        '<int:testimonial_id>/',
        views.testimonial_detail,
        name='testimonial_detail'),
    path(
        'add/',
        views.add_testimonial,
        name='add_testimonial'),
    path(
        'edit/<int:testimonial_id>/',
        views.edit_testimonial,
        name='edit_testimonial'),
    # path(
    #     'delete/<int:testimonial_id>/',
    #     views.delete_testimonial,
    #     name='delete_testimonial'),
    path(
        'delete/<pk>/',
        views.DeleteTestimonial.as_view(),
        name='delete_testimonial'),
]

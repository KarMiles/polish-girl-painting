from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.TestimonialList.as_view(),
        name='testimonials'),
    path(
        '<int:testimonial_id>/',
        views.testimonial_detail,
        name='testimonial_detail'),
    path(
        'add/',
        views.testimonial_add,
        name='testimonial_add'),
    path(
        'edit/<int:testimonial_id>/',
        views.testimonial_edit,
        name='testimonial_edit'),
    path(
        'delete/<pk>/',
        views.TestimonialDelete.as_view(),
        name='testimonial_delete'),
]

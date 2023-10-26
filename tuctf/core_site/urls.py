""" Defines the URL patterns for core_site. """

from django.urls import path

from . import views

app_name = 'core_site'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]

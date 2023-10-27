""" Defines the URL patterns for core_site. """

from django.urls import path

from . import views

app_name = 'core_site'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('2023', views.tuctf_2023, name='tuctf_2023'),
    path('rules', views.rules_2023, name='rules_2023'),
]

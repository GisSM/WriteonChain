from django.urls import path
from . import views

urlpatterns = [
    path('about_site/',views.about_site,name='about_site'),
]
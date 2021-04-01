from django.urls import path
from . import views

urlpatterns = [
     path('register/', views.register, name='register'),
     path('profilo/',views.profilo,name='profilo'),
]
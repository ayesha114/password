from django.urls import path
from . import views

urlpatterns = [
    path('', views.password, name='password'),
]
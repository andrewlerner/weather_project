from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_form, name='input_form'),
]
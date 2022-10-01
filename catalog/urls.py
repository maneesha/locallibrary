import imp
from django.urls import path
from . import views

urlpatterns = [

    # Three params for path: 
    # URL pattern is empty string, 
    # view function - function named index in views.py
    # name is used to reverse mapper so you can do this in a template:
    # <a href="{% url 'index' %}">Home</a>
    # instead of 
    # <a href="/catalog/">Home</a> 
    # which ill break if we change pattern to home page
    path('', views.index, name='index')
]
from django.conf.urls import url
from django.urls import path 

from . import views

app_name = 'seniordesign'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^seniordesign/index/*$', views.index, name='index'),
]
 

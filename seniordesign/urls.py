from django.conf.urls import url
#from django.urls import path 

from . import views
from django.contrib.auth.views import LoginView

from seniordesign.views import (index, logout_view, userCreate)


app_name = 'seniordesign'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^seniordesign/index/*$', views.index, name='index'),
    url(r'^seniordesign/dashboard/*$', views.dashboard, name='dashboard'),
    url(r'^seniordesign/interests/*$', views.interests, name='interests'),
    #The next two need their template names, add the names after the html files are added to proj
    url(r'^login/$', LoginView.as_view(template_name = "home_logged_out copy.html",redirect_field_name = "/logged_in"), name='login'),
    url(r'^loginErrors/$', LoginView.as_view(template_name = ".html",redirect_field_name = "/logged_in"), name='loginErrors'),
    url(r'^userCreate/$', userCreate ,name ="userCreate"),
    url(r'^log_out/$', logout_view ,name ="log_out"),
    

]
 

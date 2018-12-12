from django.conf.urls import url
#from django.urls import path 

from . import views
from django.contrib.auth.views import LoginView


from seniordesign.views import * #(index, logout_view, userCreate)


app_name = 'seniordesign'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/*$', views.index, name='index'),
    url(r'^login/$', LoginView.as_view(template_name = "home_logged_out copy.html",
                                       redirect_field_name = "/logged_in"), name='login'),
    url(r'^homePage/*$', views.dashboard, name='homePage'),
    url(r'^myEvents/*$', views.myEvents, name='myEvents'),
    url(r'^explore/*$', views.explore, name='explore'),
               
    #url(r'^viewProfile/*$', views.dashboard, name='viewProfile'),
    #url(r'^search/*$', views.dashboard, name='search'),
    url(r'^register/$', userCreate ,name ="register"),

    url(r'^createEvent/$', views.createEventView.as_view() ,name ="createEvent"),
    url(r'^viewEvent/$', views.viewEvent ,name ="viewEvent"),
    url(r'^viewEvent2/$', views.viewEvent2 ,name ="viewEvent2"),
    url(r'^viewEvent3/$', views.viewEvent3 ,name ="viewEvent3"),
    url(r'^viewEvent4/$', views.viewEvent4 ,name ="viewEvent4"),
               
    
    url(r'^updateProfile/$', views.editUser, name='updateProfile'),           

    url(r'^viewProfile/$', views.viewProfile, name='viewProfile'),  
    url(r'^search/$', views.search, name='search'),      
    #url(r'^viewProfile/$', views.AccountDetailView.as_view() ,name='viewProfile'),
               
    #The next two need their template names, add the names after the html files are added to proj
    
    url(r'^loginErrors/$', LoginView.as_view(template_name = ".html",redirect_field_name = "/logged_in"), name='loginErrors'),
    
    url(r'^log_out/$', logout_view ,name ="log_out"),
    

]
 

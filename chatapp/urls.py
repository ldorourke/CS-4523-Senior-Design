from django.urls import re_path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    re_path(r'^$', views.app, name='chatapp'),
    url(r'^chatapp/chat/*$', views.app, name='app'),
    re_path(r'^token', views.token, name='token'),
]
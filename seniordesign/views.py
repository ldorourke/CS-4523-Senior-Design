from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import loader
from django import forms



site_hdr = "Senior Design"

def index(request):
    return render(request, 'index.html', {'header': site_hdr})


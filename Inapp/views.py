from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')
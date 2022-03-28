from django.shortcuts import render
from .models import Category, Picture
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my gallery!')
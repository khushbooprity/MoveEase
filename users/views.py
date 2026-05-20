from django.shortcuts import render
from django import http


# Create your views here.

def index(request):
    return http.HttpResponse('Hii Index file is called')
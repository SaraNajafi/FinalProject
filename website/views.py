from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_view(request):
    return HttpResponse('<h1> home</h1>')

def about_view(request):
    return HttpResponse('<h1> about me</h1>')

def contact_view(request):
    return HttpResponse('<h1> Contact me</h1>')
    
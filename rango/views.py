from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello World, I'm Rango! </br> <a href='/rango/about/'>About</a>")

def about(request):
  return HttpResponse("Rango says here is the about page. </br> <a href='/rango/'>Home</a>")
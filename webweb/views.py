from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def root(request):
  return HttpResponse('Hello Django')

def index(request):
  return render(request, '../templates/webweb/main/index.html')

def home(request):
  return render(request, '../templates/webweb/main/index.html')


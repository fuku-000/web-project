from django.shortcuts import render

# Create your views here.

def root(request):
  return HttpResponse('Hello Django')
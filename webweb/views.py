from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
# Create your views here.

def root(request):
  return HttpResponse('Hello Django')
=======
def index(request):
    return render(request, '../templates/webweb/main/index.html')
>>>>>>> f7f2cfa8a6bd1d400f3aa9fd617b11705725410a

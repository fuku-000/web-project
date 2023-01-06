

from django.shortcuts import render

from django.views.generic import TemplateView
from django.urls import reverse_lazy
from webweb.forms import WebwebForm
from django.views.generic import CreateView

 
class IndexView(TemplateView):
    template_name = 'index.html'

class WebwebCreateView(CreateView):
    template_name = 'webweb_create.html'
    form_class = WebwebForm
    success_url = reverse_lazy('webweb:webweb_create_complete')

class WebwebCreateCompleteView(TemplateView):
    template_name = 'webweb_create_complete.html'


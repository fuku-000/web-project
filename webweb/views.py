from django.shortcuts import render

from django.views.generic import TemplateView
from django.urls import reverse_lazy
from webweb.forms import WebwebForm
 
class IndexView(TemplateView):
    template_name = 'index.html'

class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = WebwebForm
    success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'

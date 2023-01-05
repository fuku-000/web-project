from django import forms
from .models import Webweb

class WebwebForm(forms.ModelForm):
    class Meta:
        model = Webweb
        fields = ('date', 'title', 'text',)

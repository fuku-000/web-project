
from django.urls import path
from . import views
 
app_name = 'webweb'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('create/', views.WebwebCreateView.as_view(), name='webweb_create'),
    path('complete/', views.WebwebCreateCompleteView.as_view(), name='webweb_create_complete'),
]


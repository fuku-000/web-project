<<<<<<< HEAD

from django.urls import path
from . import views

urlpatterns = [
	path('', views.root, name='root'),
=======
##urls.pyはデフォルトでは作成されていないので作成すること。
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
>>>>>>> f7f2cfa8a6bd1d400f3aa9fd617b11705725410a
]
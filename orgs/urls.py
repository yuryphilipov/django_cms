from django.urls import include, path
from . import views

urlpatterns = [
	path(r'', views.home, name='home'),
	path(r'(?P<id>\d+)/', views.detail, name='detail'),
]

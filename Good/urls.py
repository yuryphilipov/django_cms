from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?:(?P<cat_id>\d+)/)?$', views.category, name='category'),
  url(r'^good/(?:(?P<good_id>\d+)/)?$', views.good, name='good'),
  url(r'^all/$', views.goods, name='goods'),
]

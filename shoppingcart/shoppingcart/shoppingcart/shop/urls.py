from django.conf.urls import url
from django.urls import path, include, re_path
from . import views
urlpatterns = [
    url(r'^(?P<productid>\d+)/$', views.product_detail, name='product_detail'),
    re_path('^$', views.product_list, name='product_list'), #daca nu mai vine nimic dupa shop leaga product list
  #  url(r'^(?P<categoryid>\d+)/$', views.product_list, name='product_list_by_category'),
   # url(r'produs/', views.product_detail, name='product_detail'),
]
from django.conf.urls import url
from django.urls import path, include, re_path
from . import views
urlpatterns = [
    url(r'^category/(?P<categoryid>\d+)/$', views.category_product_list, name='product_list_by_category'),
    url(r'^product/(?P<productid>\d+)/$', views.product_detail, name='product_detail'),
    re_path('^$', views.category_product_list, name='product_list'), #daca nu mai vine nimic dupa shop leaga product list
   # url(r'produs/', views.product_detail, name='product_detail'),
]
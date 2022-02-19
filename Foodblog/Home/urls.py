from django.urls import path
from Home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('/Products', views.home, name='products'),
    path('/Blog-single', views.home, name='blog-single'),
    path('/Blog', views.home, name='blog'),
    path('/Single-product', views.home, name='single-product'),
  
]
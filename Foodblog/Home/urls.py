from django.urls import path
from Home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('About', views.home, name='about'),
    path('Building', views.home, name='building'),
  
]
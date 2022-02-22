from django.urls import path
from Login import views


urlpatterns = [
    path('Login', views.login_request, name='login'),
  
]
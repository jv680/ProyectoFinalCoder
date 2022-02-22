from django.urls import path
from Login import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('Login', views.login_request, name='login'),
    path('Logout', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
  
]
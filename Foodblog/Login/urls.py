from django.urls import path
from Login import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('Login', views.login_request, name='login'),
    path('Logout', login_required(LogoutView.as_view(template_name='logout.html')), name = 'logout'),
  
]
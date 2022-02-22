from django.urls import path
from Profiles import views


urlpatterns = [
    path('Profiles', views.profiles, name='profiles'),
  
]
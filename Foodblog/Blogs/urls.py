from django.urls import path
from Blogs import views


urlpatterns = [
    path('Blog', views.blog, name='blog'),
    path('Blogadd', views.addreceta, name='blogadd'),
    path('Deletereceta/<id_receta>', views.deletereceta, name='deletereceta'),
    path('updateRecetas/<id_receta>', views.updateRecetas, name='updaterecetas'),
  
]
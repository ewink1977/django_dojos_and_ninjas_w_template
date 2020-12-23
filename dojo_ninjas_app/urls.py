from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('newdojo', views.newdojo),
    path('newninja', views.newninja),
    path('delete/<int:dojotodel>', views.deletedojo),
]
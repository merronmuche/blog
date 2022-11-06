from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
   
    path('', views.list),
    path('add/', views.add)
]
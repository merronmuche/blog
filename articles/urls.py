from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.list, name='list'),
    path('add/', views.add),
    path('<id>/',views.detail, name='detail'),
    
]
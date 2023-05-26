from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name="home"),
    path('weather/', views.weather_app,name="weather"),
    
]
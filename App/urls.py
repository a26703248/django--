from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('hello/', views.hello),
    path('html_tag/', views.html_tag),
    path('index/', views.index),
    path('home/', views.home),
]

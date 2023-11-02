from django.contrib import admin
from django.urls import path, include
from app_practice import views

app_name = 'app_practice'

urlpatterns = [
    path('root/', views.root, name='root'),
]
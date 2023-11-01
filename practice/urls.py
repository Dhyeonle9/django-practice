"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_practice import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # django 친해지기
    path('start/', views.start),
    path('root/', views.root),
    # index 페이지
    path('index/', views.index),
    # CRUD 구현 연습
    # Read (전체글)
    path('board/', views.board),
    # Read (게시물 보기)
    path('posts/<int:id>/', views.content),
    # Create (새게시물 작성)
    path('posts/new/', views.new),
    # Create (게시물 등록)
    path('posts/create/', views.create),
    # Update (게시물 가져와서 내용수정)
    path('posts/<int:id>/edit/', views.edit),
    # Update (수정내용 등록)
    path('posts/<int:id>/update/', views.update),
    # Delete (게시물 삭제)
    path('posts/<int:id>/delete/', views.delete),
]

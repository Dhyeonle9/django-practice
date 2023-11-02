from django.contrib import admin
from django.urls import path, include
from board import views 

app_name = 'board'
urlpatterns = [

    # CRUD 구현 연습
    # Read (전체글)
    path('', views.index, name='b_index'),
    # Read (게시물 보기)
    path('<int:id>/', views.content, name='content'),
    # Create (새게시물 작성)
    path('new/', views.new, name='new'),
    # Create (게시물 등록)
    path('create/', views.create, name='create'),
    # Update (게시물 가져와서 내용수정)
    path('<int:id>/edit/', views.edit, name='edit'),
    # Update (수정내용 등록)
    path('<int:id>/update/', views.update, name='update'),
    # Delete (게시물 삭제)
    path('<int:id>/delete/', views.delete, name='delete'),
]
from django.contrib import admin
from django.urls import path, include
from board import views 

app_name = 'board'
urlpatterns = [
    # 게시판
    # Read (전체글)
    path('', views.index, name='b_index'),
    # Read (게시물 보기)
    path('<int:id>/', views.content, name='content'),
    # Create (게시물 등록)
    path('create/', views.create, name='create'),
    # Update (수정내용 등록)
    path('<int:id>/update/', views.update, name='update'),
    # Delete (게시물 삭제)
    path('<int:id>/delete/', views.delete, name='delete'),

    # 댓글
    # Create
    path('<int:post_id>/comments/create/', views.comment_create, name='comment_create'),
    # delete
    path('<int:post_id>/comments/<int:id>/delete/', views.comment_delete, name='comment_delete'),
]
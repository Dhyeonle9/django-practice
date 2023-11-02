from django.shortcuts import render, redirect
from .models import Post

# CRUD 구현 연습
# 게시판 전체페이지
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,  
    }
    return render(request, 'board_index.html', context)
# 게시물 보기

def content(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'content.html', context)

# 새게시물 작성
def new(request):
    return render(request, 'new.html')
# 작성등록
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()
    return redirect('board:content', id=post.id)
# 게시글 수정
def edit(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'edit.html', context)
# 수정내용 등록
def update(request, id):
    title = request.GET.get('title')
    content = request.GET.get('content')
    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()
    return redirect('board:content', id=post.id)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('board:b_index')
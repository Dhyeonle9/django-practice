from django.shortcuts import render, redirect
from .models import Post
def start(request):
    greeting = '안녕하세요'
    result = {
        'greeting': greeting,
    }
    return render(request, 'start.html', result)

def root(request):
    
    input = request.GET.get('input')
    if input:
        rootnum = int(input) ** 0.5
        if rootnum == int(rootnum):
            rootnum = int(rootnum)
        result = {
            'input': input,
            'rootnum': rootnum,
        }
        return render(request, 'root.html', result)
    else:
        return render(request, 'root.html')
def index(request):
    return render(request, 'index.html')
# CRUD 구현 연습
# 게시판 전체페이지
def board(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,  
    }
    return render(request, 'board.html', context)
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
    return redirect(f'/posts/{post.id}')
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
    return redirect(f'/posts/{post.id}/')
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(f'/board/')
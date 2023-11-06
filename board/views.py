from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

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
    form = CommentForm

    # comments = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        # 'comments': comments,
    }
    return render(request, 'content.html', context)

# 작성등록
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('board:content', id=post.id)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)
    
# 수정내용 등록
def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('board:content', id=post.id)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('board:b_index')

def comment_create(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post_id = post_id
        comment.save()
        return redirect('board:content', id=post_id)

def comment_delete(request, post_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('board:content', id=post_id)
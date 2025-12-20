from django.shortcuts import render, get_object_or_404
from .models import Post

def home_page(request):
    return render(request, 'home_page.html')

def blog_page(request):
    return render(request, 'blog_page.html')

def posts_page(request):
    return render(request, 'posts_page.html')

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'slug': slug})
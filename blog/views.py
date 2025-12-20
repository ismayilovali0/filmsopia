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

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    """Bir postun tam detalını göstərir"""
    post = get_object_or_404(Post, pk=pk)
    
    previous_post = Post.objects.filter(pk__lt=post.pk).order_by('-pk').first()
    next_post = Post.objects.filter(pk__gt=post.pk).order_by('pk').first()
    
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
    }
    return render(request, 'blog/post_detail.html', context)
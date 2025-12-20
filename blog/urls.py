from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='home_page'), 
    path('blog/', views.blog_page, name='blog_page'),
    path('aslam/', views.posts_page, name='posts_page'),
    path('post/<slug>/', views.post, name='post'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
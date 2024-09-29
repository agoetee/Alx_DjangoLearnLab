from django.urls import path
from .views import PostList, PostDetail, PostBlog,listPost

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/', PostBlog, name="post"),
    path('getposts/', listPost, name="post")
]

from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('comment_update/<int:id>', views.comment_update, name='comment_update'),
    path('comment/<int:pk>/update',CommentUpdateView.as_view(), name='comment-update' ),
    path('about/', views.about, name="blog-about"),

]
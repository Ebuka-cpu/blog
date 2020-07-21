from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import *
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


# Create your views here.
# LISTING ALL OUR POSTS IN THE HOME PAGE
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']     # MAKING OUR MOST RECENT POSTS APPEAR TOP
    paginate_by = 5        # ADDING PAGINATION TO OUR BLOG POST


# GETTING ALL THE POSTS MADE BY A USER
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


# CREATING A NEW POST
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# UPDATING OUR POSTS
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# DELETING OUR POSTS
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required(login_url='login')
def comment_update(request):
    comment = Comment.objects.all()
    return render(request, 'comment_update.html', {'data': comment})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    fields = ['content']
    success_url = '/index'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def get_success_message(self, cleaned_data):
        return 'Updated successfully'



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



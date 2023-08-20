from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User

from .models import *
from .forms import *


class PostList(ListView):
    model = Post
    ordering = 'post_creation_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_not_author'] = not self.request.user.groups.\
    #         filter(name='authors').exists()
    #     return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_author = self.request.user
        return super().form_valid(form)


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

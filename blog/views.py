from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name =  'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # template_nameなしで(appの名前)/(modelの名前)_(viewの名前).htmlにすると自動で参照してくる
    # blog/post_detail.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        print("Form", form)
        print("Form Instance", form.instance)
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    print("Out of Form_valid")
    def form_valid(self, form):
        print("Form", form)
        print("Form Instance", form.instance)
        print("Form author", form.instance.author)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        print("Test_func")
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        print("Test_func")
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
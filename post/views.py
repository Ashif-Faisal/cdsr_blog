from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import post
# Create your views here.
class HomePage(ListView):
    model = post
    template_name = 'posts/home.html'
    context_object_name = 'data'
    ordering = ['-id']


class DetailsView(DetailView):
    model = post
    template_name = "posts/details.html"


class CreatePost(CreateView):
    model = post
    fields = ['title','content']
    template_name = "posts/newpost.html"
    success_url = "/"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class DeletePost(DeleteView):
    model = post
    template_name = "posts/deletepost.html"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = "/"


class UpdatePost(UpdateView):
    model = post
    fields = ['title','content']
    template_name = "posts/newpost.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = "/"
    

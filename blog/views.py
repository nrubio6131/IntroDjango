from ast import Div
from contextlib import redirect_stderr
from http.client import ImproperConnectionState
import imp
from importlib.resources import path
from multiprocessing import context
from turtle import update
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm, PostCreateUser
from .models import Post, user
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwarsg):
        posts = Post.objects.all()
        context={
            'posts':posts
        }
        return render(request, 'blog_list.html', context)

class BlogCreateVieww(View):
    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)

    def post (self, request, *args, **kwargs):
        if request.method == "POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('tittle')
                content = form.cleaned_data.get('content')
                p, created = Post.objects.get_or_create(tittle = title, content = content)
                p.save()
                return redirect('blog:home')
        context={
            
        }
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post':post
        }
        return render(request, 'blog_detail.html', context)

class BlogUpdateView(UpdateView):
    model= Post
    fields= ['tittle','content']
    template_name = 'blog_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail',kwargs={'pk':pk})

class BlogDeleteView(DeleteView):
    model = Post
    template_name='blog_delete.html'
    success_url = reverse_lazy('blog:home')

class BlogCreateUser(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateUser()
        context={
            'form':form
        }
        return render(request, 'blog_create_user.html', context)
    
    def post (self, request, *args, **kwargs):
        if request.method == "POST":
            form = PostCreateUser(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                number = form.cleaned_data.get('number')
                decimal = form.cleaned_data.get('decimal')
                email = form.cleaned_data.get('email')
                p, created = user.objects.get_or_create(name=name,number=number,decimal=decimal,email=email)
                p.save()
                return redirect('blog:home')
            else:
                context={
                    'alert':"los datos no son correctos, verificar",
                    'form':form
                }
                return render(request, 'blog_create_user.html', context)












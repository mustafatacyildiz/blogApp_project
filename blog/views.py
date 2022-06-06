from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm


def post_list(request):
    posts  = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_create(request):
    form = BlogForm() # boş form render edeceğiz
    if request.method == 'POST':          
        print(request.POST)				   
        form = BlogForm(request.POST)   
        if form.is_valid():				   
            form.save()
            return redirect("list")					   
    context = {
        'form' : form
    }
    return render(request, 'blog/post_create.html', context)


def blog_detail(request, id):        
    post = Blog.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def blog_update(request, id):
    post =Blog.objects.get(id=id)
    form = BlogForm(instance=post)
    if request.method== "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("list")   
    context = {
        'form':form,
    }
    return render(request, 'blog/post_update.html', context)


def blog_delete(request, id):
    post = Blog.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect("list")
    return render(request, "blog/post_delete.html") 


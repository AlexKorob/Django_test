from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "posts/index.html", context={"posts": posts, "categories": categories})


def post_profile(request, post_id):
    categories = Category.objects.all()
    post = Post.objects.get(id=post_id)
    print("POST: ", post.title)
    return render(request, "posts/post_details.html", context={"post":post, "categories": categories})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect("/posts")
        return render(request, "posts/add_post.html", context={"errors": form.errors})
    return render(request, "posts/add_post.html")

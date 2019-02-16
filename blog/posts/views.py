import time
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.utils.translation import gettext_lazy as _


cache = caches["default"]


class PostListView(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"
    time.sleep(5)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostCategoryListView(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return self.model.objects.filter(category_id=self.kwargs["category_id"])


@cache_page(3600)   # time cache 3600
def index(request):
    posts = Post.objects.all().select_related("category")
    categories = Category.objects.all()
    return render(request, "posts/index.html", context={"posts": posts, "categories": categories})


def post_profile(request, post_id):
    categories = Category.objects.all()
    post = Post.objects.get(id=post_id)
    cnt = request.session.get("cnt", 0)
    cnt += 1
    request.session["cnt"] = cnt
    return render(request, "posts/post_details.html", context={"post":post, "categories": categories, "cnt": cnt})


def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # post = Post.objects.create(**form.cleaned_data)
            # post.save()
            form.save()
            return redirect("/posts")
        return render(request, "posts/add_post.html", context={"errors": form.errors, "form": form})
    return render(request, "posts/add_post.html", context={"form": form})


def logining(request):
    if request.method == "GET":
        c = cache.get("cached_key_logining")
        if c is None:
            time.sleep(5)
            c = cache.set("cached_key_logining", render(request, "posts/login.html", {}))
        return c
    elif request.method == "POST":
        u = authenticate(username=request.POST["username"], password=request.POST["password"])
        if u is None:
            raise Http404()
        login(request, u)
        return redirect("/posts/")


def return_localization_str(request):
    string_2 = _("Hello World")
    string = _("test %(test)d") % {"test": 1}
    return HttpResponse(string_2)

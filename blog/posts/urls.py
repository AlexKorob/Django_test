from django.urls import path, include
from django.views.decorators.cache import cache_page    # <-- for cache CBV

from . import views
app_name="posts"

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.logining, name="login"),
    path('<int:post_id>', views.post_profile, name = 'post_detail'),
    path('add_post/', views.add_post, name = 'add_post'),
    path('str/', views.return_localization_str, name='str'),
    path("clbv/", cache_page(3600)(views.PostListView.as_view()), name='post_list'),
    path("category/<int:category_id>", views.PostCategoryListView.as_view(), name="post_category_list"),
]

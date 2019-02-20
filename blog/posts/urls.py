import rest_framework
from django.urls import path, include
from django.conf.urls import url
from django.views.decorators.cache import cache_page    # <-- for cache CBV
from . import views
from . import api_views

app_name="posts"

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.logining, name="login"),
    path('<int:post_id>', views.post_profile, name = 'post_detail'),
    path('add_post/', views.add_post, name = 'add_post'),
    path('str/', views.return_localization_str, name='str'),
    path("clbv/", cache_page(3600)(views.PostListView.as_view()), name='post_list'),
    path("category/<int:category_id>", views.PostCategoryListView.as_view(), name="post_category_list"),

    path("api-posts/", api_views.PostList.as_view(), name="api_posts"),
    path("api-post-detail/<int:pk>/", api_views.PostDetail.as_view(), name="api_post_detail"),
    path("api-categories/", api_views.CategoryList.as_view(), name="api_categories"),
    path("api-category-detail/<int:pk>/", api_views.CategoryDetail.as_view(), name="api_categories_detail"),

    url(r'^api-auth/', include('rest_framework.urls')),
    path("users/", api_views.UserList.as_view()),
    path("user-detail/<int:pk>", api_views.UserDetail.as_view()),
]

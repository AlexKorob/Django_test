from django.urls import path

from . import views
app_name="posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>', views.post_profile, name = 'post_detail'),
    path('add_post/', views.add_post, name = 'add_post'),
    path("clbv/", views.PostListView.as_view(), name='post_list'),\
    path("category/<int:category_id>", views.PostCategoryListView.as_view(), name="post_category_list")
]

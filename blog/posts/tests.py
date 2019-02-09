from django.test import TestCase
from .models import Category, Post
from django.urls import reverse


class PostTestCase(TestCase):
    category_name = "test_category"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name=cls.category_name, is_active=True)

    def test_post_list(self):
        p = Post.objects.create(title="Test", status=20, content="LLL", category=self.category_name)
        post_list_url = reverse("posts:index")
        r = self.client.get(post_list_url)
        self.assertEquals(r.status_code, 200)
        self.assertEquals(len(r.context["posts"]), 1)

    def test_post_add(self):
        post_params = {"title": "test_post", "content": "LLL", "status": 20, "category": self.category_name}
        url = reverse("posts:add_post")
        p = Post.objects.count()
        r = self.client.post(url, data=post_params)
        self.assertEquals(Post.objects.count(), p + 1)
        self.assertEquals(r.status_code, 200)

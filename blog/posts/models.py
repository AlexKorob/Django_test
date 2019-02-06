from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import TagItem


class Post(models.Model):
    STATUS_DRAFT = 10
    PUBLISHED = 20
    REJECTED = 30

    STATUS = [
       (STATUS_DRAFT, "draft"),
       (PUBLISHED, "published"),
       (REJECTED, "rejected")
    ]

    title = models.CharField(max_length=100, unique=True, error_messages={'required': 'Заголовок не должен быть пустым',
                                                                          'unique': 'Такой заголовок уже существует'})
    content = models.TextField(error_messages={'required': 'Поле контента не может быть пустым'})
    status = models.SmallIntegerField(choices=STATUS, default=STATUS_DRAFT)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, related_name="posts")
    keywords = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    tags = GenericRelation(TagItem)

    class Meta:
       ordering = ['-updated_on']

    def __str__(self):
       return self.title


class Category(models.Model):
    name = models.CharField(max_length=40)
    metakeywords =  models.TextField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

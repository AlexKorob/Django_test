from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Tag(models.Model):
    name = models.CharField(max_length=50)


class TagItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tag_items")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

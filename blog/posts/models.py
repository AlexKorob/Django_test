from django.db import models


class Post(models.Model):
   title = models.CharField(max_length=100, unique=True)
   content = models.TextField()
   keywords = models.TextField(max_length=500, blank=True)
   created_on = models.DateTimeField(auto_now_add=True)
   updated_on = models.DateField(auto_now=True)

   class Meta:
       ordering = ['-updated_on']

   def __str__(self):
       return self.title

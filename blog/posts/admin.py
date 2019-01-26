from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ('title', 'created_on')

admin.site.register(Post, PostAdmin)

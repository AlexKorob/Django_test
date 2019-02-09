from django.contrib import admin
from tags.models import TagItem, Tag


class TagAdmin(admin.ModelAdmin):
    pass


class TagItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(TagItem, TagItemAdmin)

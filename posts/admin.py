from django.contrib import admin
from .models import Post, PostLike
# Register your models here.


class PostLikeAdmin(admin.TabularInline):
    model = PostLike

class PostAdmin(admin.ModelAdmin):
    inlines=[PostLikeAdmin]
    list_display=['__str__', 'user'] # shows user and posts in table. to show real content text add __str__ in clas Post
    search_fields=['user__username', 'content'] # created search field to filter by on /admin/posts
    class Meta:
        model=Post

admin.site.register(Post, PostAdmin)
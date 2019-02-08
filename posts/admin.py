"""post admin classes"""

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#models
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """post admin"""

    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user',)
    list_editable = ('title','photo')


    list_filter = (
    'created',
    'modified',
    )

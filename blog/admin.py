from django.contrib import admin

# Register your models here.

from .models import Post, user
admin.site.register(Post)
admin.site.register(user)
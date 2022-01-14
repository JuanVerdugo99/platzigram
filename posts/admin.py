"""Post admin classes."""

# Django
from django.contrib import admin
from .models import Post

admin.site.register(Post)

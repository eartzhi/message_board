from django.contrib import admin
from .models import Category, Post, Author, Response

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Response)
admin.site.register(Category)


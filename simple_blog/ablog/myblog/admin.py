from django.contrib import admin
# from models.py Post Class
from .models import Post, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
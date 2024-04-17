from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        #return reverse('article_detail', args=(str(self.id)))
        return reverse('home')

# Create a bunch of blog post. If some one is detleted, all his post will be removed
class Post(models.Model):
    title = models.CharField(max_length=255)
    #title_tag = models.CharField(max_length=255, default="Blog Post") # si agregamos un campo al modelo, debemos darle un valor por defecto
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=255, default="coding")

    def __str__ (self):
        return self.title  + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article_detail', args=(str(self.id)))
        return reverse('home')
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
    
class Consumos(models.Model):
    id = models.IntegerField(primary_key=True)
    alcance = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50)
    subcategoria = models.CharField(max_length=100)
    fuente = models.CharField(max_length=255)
    cantidad_fuente = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    linkRespaldo = models.CharField(max_length=255)
    comentarios = models.CharField(max_length=255)
    huellaChile = models.CharField(max_length=255)

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
class Proyectos(models.Model):
    id = models.IntegerField(primary_key=True)
    consumo = models.CharField(max_length=255)
    HuellaDeCarbono = models.CharField(max_length=255)
    HuellaHidrica = models.CharField(max_length=255)
    HuellaFinanciera = models.CharField(max_length=255)

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Alcances(models.Model):
    descripcion = models.CharField(max_length=255)
    categorias = models.CharField(max_length=255)
    tipoDeAlcance = models.CharField(max_length=255)

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Categorias(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    ##subcategorias = models.CharField(max_length=255) ### Quizas este campo no va
    
    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class SubCategorias(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    categorias = models.CharField(max_length=255) 
    
    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
class Fuente(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    combustible = models.CharField(max_length=255)
    UnidadFuente = models.CharField(max_length=255)
    FactorEmision = models.CharField(max_length=255)
    Alcance = models.CharField(max_length=255)
    Categoria = models.CharField(max_length=255)
    Subcategoria = models.CharField(max_length=255) 
    
    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')


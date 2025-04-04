from django.db import models


# Create your models here.
class Categorias(models.Model):
    categorias_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    descricao = models.TextField(max_length=255, blank=True)
    categoria_image = models.ImageField(upload_to="photos/categories/", blank=True)

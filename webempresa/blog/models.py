from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User # It contains all users registered in the admin panel

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published_on = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    
    """
    Introducing Entity Relations (Using Foreign key)
    "on_delete" works to tell what will happen if any content's author is deleted. In this case, this option will delete
    in cascade all entries that a specific author had.
    To allow to have any empty field in the database, you need 'null=True, blank=True'.
    """
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")

    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created_on"]

    def __str__(self): 
        return self.title

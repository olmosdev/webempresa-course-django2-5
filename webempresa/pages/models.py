from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    # To not sort the models automatically, but in an order established by the user
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ["order", "title"] # Redefining the priority order

    def __str__(self): 
        return self.title

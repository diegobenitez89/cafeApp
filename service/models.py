from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    image = models.ImageField(verbose_name='imagenes',upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering =['-created']
    def __str__(self):
        return self.title



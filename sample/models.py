from django.db import models

# Create your models here.
class Sample(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    class Meta:
        verbose_name = "Sample"
        verbose_name_plural = "Samples"
        ordering =['-created']
    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True)
    apellido = models.CharField(max_length=100, verbose_name='apellido')
    telefono = models.CharField(max_length=100,verbose_name='telefono')
    email = models.CharField(max_length=100, verbose_name='email')

    def __str__(self):
        fila = "nombre:"+self.nombre+"-"+"apellido:"+self.apellido+"-"+"telefono:"+self.telefono+"email:"+self.email
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)
    


class Producto(models.Model):
    id= models.AutoField(primary_key=True)
    url_imagen = models.URLField()
    nombre_producto = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')

    def __str__(self):
        return str(self.nombre_producto)
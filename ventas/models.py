from django.db import models
from django.conf import settings

class Producto(models.Model):
    Nombre =  models.TextField( null=False,blank=False)
    Descripcion = models.TextField(null=False,blank=False)
    Stock = models.IntegerField(null=False,blank=False)
    Precio = models.FloatField(null=False,blank=False)

# Create your models here.
class Detalle_Venta(models.Model):
    #id_movimiento =ForeignKey()
    id_producto = models.ForeignKey(Producto ,on_delete=models.CASCADE )
    cantidad = models.IntegerField()
    total = models.FloatField()


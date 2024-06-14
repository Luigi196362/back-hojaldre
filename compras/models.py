from django.db import models
from django.conf import settings

class Ingrediente(models.Model):
    Nombre =  models.TextField( null=False,blank=False)
    Descripcion = models.TextField(null=False,blank=False)
    Stock = models.IntegerField(null=False,blank=False)

# Create your models here.
class Detalle_Compra(models.Model):
    #id_movimiento =ForeignKey()
    id_ingrediente = models.ForeignKey(Ingrediente ,on_delete=models.CASCADE )
    cantidad = models.IntegerField()
    total = models.FloatField()
    #id_proveedor =ForeignKey()

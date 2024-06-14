import graphene
from graphene_django import DjangoObjectType

from ventas.models import Detalle_Venta,Producto


class Detalle_Venta_Type(DjangoObjectType):
    class Meta:
        model = Detalle_Venta

class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto

class Query(graphene.ObjectType):
    Detalles = graphene.List( Detalle_Venta_Type )
    Productos = graphene.List( ProductoType )

    def resolve_Detalles(self, info, **kwargs):
        return Detalle_Venta.objects.all()
        
    def resolve_Productos(self, info, **kwargs):
        return Producto.objects.all()



class CreateProducto(graphene.Mutation):

    id = graphene.Int()
    Nombre=graphene.String()
    Descripcion=graphene.String()
    Stock=graphene.Int()
    Precio=graphene.Float()

    class Arguments:
        Nombre=graphene.String(required=True)
        Descripcion=graphene.String(required=True)
        Stock=graphene.Int(required=True)
        Precio=graphene.Float(required=True)
        
    def mutate(self, info, Nombre,Descripcion,Stock, Precio):

        producto = Producto( Nombre=Nombre,
                      Descripcion=Descripcion,
                      Stock=Stock, 
                      Precio=Precio,
                   )
        producto.save()

        return CreateProducto(
            id=producto.id,
            Nombre=producto.Nombre,
            Descripcion=producto.Descripcion,
            Stock=producto.Stock,
            Precio=producto.Precio         
        )
    
class DeleteProducto(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        producto_id = graphene.Int(required=True)

    def mutate(self, info, producto_id):
        producto = Producto.objects.get(pk=producto_id)
        producto.delete()
        return DeleteProducto(id=producto_id)


class Mutation(graphene.ObjectType):
    create_producto = CreateProducto.Field()
    delete_producto = DeleteProducto.Field()

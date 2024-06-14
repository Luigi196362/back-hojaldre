import graphene
from graphene_django import DjangoObjectType

from compras.models import Detalle_Compra,Ingrediente


class Detalle_Compra_Type(DjangoObjectType):
    class Meta:
        model = Detalle_Compra

class IngredienteType(DjangoObjectType):
    class Meta:
        model = Ingrediente


class Query(graphene.ObjectType):
    Detalles = graphene.List( Detalle_Compra_Type )
    Ingredientes = graphene.List( IngredienteType )

    def resolve_Detalles(self, info, **kwargs):
        return Detalle_Compra.objects.all()
        
    def resolve_Ingredientes(self, info, **kwargs):
        return Ingrediente.objects.all()


class CreateIngrediente(graphene.Mutation):

    id = graphene.Int()
    Nombre=graphene.String()
    Descripcion=graphene.String()
    Stock=graphene.Int()
    

    class Arguments:
        Nombre=graphene.String(required=True)
        Descripcion=graphene.String(required=True)
        Stock=graphene.Int(required=True)
        
        
    def mutate(self, info, Nombre,Descripcion,Stock):

        ingrediente = Ingrediente( Nombre=Nombre,
                      Descripcion=Descripcion,
                      Stock=Stock, 
                      
                   )
        ingrediente.save()

        return CreateIngrediente(
            id=ingrediente.id,
            Nombre=ingrediente.Nombre,
            Descripcion=ingrediente.Descripcion,
            Stock=ingrediente.Stock,
        )
    
class DeleteIngrediente(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        ingrediente_id = graphene.Int(required=True)

    def mutate(self, info, ingrediente_id):
        ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
        ingrediente.delete()
        return DeleteIngrediente(id=ingrediente_id)


class Mutation(graphene.ObjectType):
    create_ingrediente = CreateIngrediente.Field()
    delete_ingrediente = DeleteIngrediente.Field()

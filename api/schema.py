import compras
import compras.schema
import graphene
import graphql_jwt
import ventas.schema
import users.schema


class Query(users.schema.Query, 
            ventas.schema.Query,
            compras.schema.Query,
            graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation,
               compras.schema.Mutation,
                ventas.schema.Mutation,
               graphene.ObjectType):
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
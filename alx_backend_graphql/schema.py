import graphene



class Query(CRMQuery, graphene.ObjectType)
hello = graphene.String(defualt_value="Hello,GraphQL!")


schema = graphene.Schema(query=Query)

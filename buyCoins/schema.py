import graphene

from calculatePrice.schema import calculate_query


class Query(calculate_query.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

import graphene


class CalculateType(graphene.ObjectType):
    type = graphene.Int()
    margin = graphene.Float()
    exchangeRate = graphene.Float()


class Query(graphene.ObjectType):
    calculatePrice = graphene.Field(
        CalculateType,
        id=graphene.String(required=True))

    def resolve_calculatePrice(self, info, **kwargs):
        return {kwargs}

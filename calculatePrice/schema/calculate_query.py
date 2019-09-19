import graphene
from calculatePrice.utils.requests import current_bitcoin_price


class TypeEnum(graphene.Enum):
    """
        Enum field for the type field
    """
    BUY = 'buy'
    SELL = 'sell'


class CalculatePrice(graphene.ObjectType):
    """
        Calculate price objectType that declares
        the Calculate price field
    """
    choice_type = graphene.String()
    margin = graphene.Float()
    exchange_rate = graphene.Float()
    calculated_price = graphene.Float()


class Query(graphene.ObjectType):
    """
     Graphene query for calculating bitcoin exchange rate
    """
    calculate_price = graphene.Field(
        CalculatePrice,
        choice_type=graphene.Argument(TypeEnum, required=True),
        margin=graphene.Float(),
        exchange_rate=graphene.Float()
    )

    def resolve_calculate_price(self, *args, **kwargs):
        """
        This method calculates the exchange rate of bitcoin in NGN
        based on user inputs
        :param args: null
        :param kwargs: choice_type, margin, computed_margin
        :return: calculated_price
        """
        choice_type = kwargs.get('choice_type')
        margin = kwargs.get('margin')
        computed_margin = margin/100
        exchange_rate = kwargs.get('exchange_rate')
        current_price = current_bitcoin_price()
        if choice_type == 'sell':
            computed_price = current_price - computed_margin
            calculated_price = computed_price * exchange_rate
        else:
            computed_price = current_price + computed_margin
            calculated_price = computed_price * exchange_rate

        return CalculatePrice(
            calculated_price=calculated_price
        )

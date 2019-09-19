from graphql import GraphQLError
import requests


def current_bitcoin_price():
    """
    Makes an GET request to return the current prices of bitcoin
    :return: The current bitcoin rate in USD
    """
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if response.status_code == 404:
        raise GraphQLError('Exchange Rate Resource not found, try again later..')
    data = response.json()
    return data['bpi']['USD']['rate_float']

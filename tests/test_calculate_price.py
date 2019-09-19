import json
from django.test import TestCase, Client
from tests.test_fixtures.calculate_price_fixture import calculate_price

# Create your tests here.


class CalculatePriceTest(TestCase):
    """
    Bitcoin Exchange rate calculation
    """

    @classmethod
    def query(cls, query: str = None):
        # Method to run all queries and mutations for tests.
        cls.client = Client()
        body = dict()
        body['query'] = query
        response = cls.client.post(
            '/buyCoins/', json.dumps(body), content_type='application/json')
        json_response = json.loads(response.content.decode())
        return json_response

    def test_user_request_BUY(self):
        """ testing when user type is BUY"""
        data = {
            'choice_type': 'BUY',
            'margin': 2,
            'exchange_rate': 3
        }
        resp = self.query(
            calculate_price.format(**data))
        self.assertIn('data', resp)
        self.assertIn('calculatedPrice', resp['data']['calculatePrice'])
        self.assertIsNotNone(resp['data']['calculatePrice']['calculatedPrice'])

    def test_user_request_SELL(self):
        """ testing when user type is SELL"""
        data = {
            'choice_type': 'SELL',
            'margin': 3,
            'exchange_rate': 4
        }
        resp = self.query(
            calculate_price.format(**data))
        self.assertIn('data', resp)
        self.assertIn('calculatedPrice', resp['data']['calculatePrice'])
        self.assertIsNotNone(resp['data']['calculatePrice']['calculatedPrice'])

    def test_bitcoin_exchange_404(self):
        """ test if the request returns 404"""
        resp = self.client.get(
            'https://api.coindesk.com/v1/bpi/currentprice.json==')
        self.assertEqual(resp.status_code, 404)

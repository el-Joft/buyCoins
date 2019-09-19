calculate_price = '''
        query {{
 calculatePrice(
  choiceType: {choice_type},
  margin: {margin},
  exchangeRate: {exchange_rate}
) {{
  calculatedPrice
}}
}}
            '''

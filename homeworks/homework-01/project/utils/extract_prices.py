def extract_prices(products):
    return map(lambda x: x.get_price(), products)

from models.product import Product
from utils.extract_prices import extract_prices


def test_extract_prices():
    products = [
        Product('a', 'x', 1),
        Product('b', 'x', 3),
        Product('c', 'y', 2),
    ]
    prices = [1, 2, 3]

    received = extract_prices(products)

    assert sorted(prices) == sorted(received)

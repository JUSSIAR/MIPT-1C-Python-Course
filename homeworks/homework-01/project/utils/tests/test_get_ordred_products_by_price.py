from models.product import Product
from utils.get_ordered_products_by_price import get_ordered_products_by_price


def test_get_ordered_products_by_price():
    products = [
        Product('p1', 'c1', 2),
        Product('p2', 'c2', 1),
        Product('p3', 'c1', 3),
    ]

    received = get_ordered_products_by_price(products)

    assert received[0].price == 3
    assert received[1].price == 2
    assert received[2].price == 1

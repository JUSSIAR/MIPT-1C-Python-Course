from models.product import Product
from utils.select_products_by_category import select_products_by_category


def test_select_products_by_category():
    category1 = 'c1'
    category2 = 'c2'
    products = [
        Product('p1', category1, 2),
        Product('p2', category2, 1),
        Product('p3', category1, 3),
    ]

    received = select_products_by_category(products, category2)

    assert len(received) == 1
    assert received[0].category == category2
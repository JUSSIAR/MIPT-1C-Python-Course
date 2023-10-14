def get_ordered_products_by_price(products):
    return sorted(products, key=lambda x: -x.get_price())

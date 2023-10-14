def select_products_by_category(products, category):
    return list(filter(lambda x: x.category == category, products))

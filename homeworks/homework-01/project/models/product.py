class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category):
        pass

    def edit_price(self, new_price):
        pass

    def set_sale(self, sale):
        pass

    def cancel_sale(self):
        pass

    def get_price(self):
        # Это не тупо геттер - тут надо учесть скидку и еще то, что скидка указана в процентах
        pass

    def __repr__(self):
        pass

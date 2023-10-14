class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category: str) -> None:
        self.category = new_category

    def edit_price(self, new_price: int) -> None:
        self.price = new_price

    def set_sale(self, sale: int) -> None:
        self.sale = sale

    def cancel_sale(self) -> None:
        self.sale = 0

    def get_price(self) -> int:
        return self.price * (100 - self.sale) / 100

    def __repr__(self) -> str:
        return "name={}, category={}. price={}. sale={}".format(self.name, self.category, self.price, self.sale)

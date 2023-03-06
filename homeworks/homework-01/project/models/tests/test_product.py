from models.product import Product


class TestProduct:
    def setup(self):
        self.product = Product('Prod1', 'hard', 10)

    def test_edit_category(self):
        self.product.edit_category('soft')
        assert self.product.category == 'soft'

    def test_edit_price(self):
        self.product.edit_price(11)
        assert self.product.price == 11

    def test_set_sale(self):
        self.product.set_sale(10)
        assert self.product.sale == 10
        assert self.product.get_price() == 9

    def test_cancel_sale(self):
        self.product.set_sale(10)
        self.product.cancel_sale()
        assert self.product.sale == 0

    def test_get_price(self):
        assert self.product.get_price() == 10

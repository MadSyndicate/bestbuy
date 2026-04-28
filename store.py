from products import Product

class Store:
    """Stores products and their quantity"""
    def __init__(self, products=None):
        if products is None:
            products = list()
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> list[Product]:
        return [
            product for product in self.products if product.is_active()
        ]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        total_price = 0.0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product not in store")

            if not product.is_active():
                raise ValueError("Product is not active")

            total_price += product.buy(quantity)

        return total_price

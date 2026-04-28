
class Product:
    """Product class representing purchasable store objects"""
    def __init__(self, name, price, quantity):

        if not isinstance(name, str):
            raise TypeError("Product name must be a string")
        if len(name) < 1:
            raise ValueError("Product name must not be empty")

        if not isinstance(price, float) and not isinstance(price, int):
            raise TypeError("Product price must be a number")
        if float(price) < 0.0:
            raise ValueError("Product price must be positive")

        if not isinstance(quantity, int):
            raise TypeError("Product quantity must be a number")
        if quantity < 0:
            raise ValueError("Product quantity must be positive")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity) -> None:
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def show(self) -> None:
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough products on stock")
        if quantity < 0:
            raise ValueError("Product quantity must be positive")

        self.quantity -= quantity
        return self.price * quantity

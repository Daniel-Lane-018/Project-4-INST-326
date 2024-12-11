class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    def calculate_discount(self):
        return 0
    
    def final_price(self):
        return self._price * 0.10
    
    class Electronics():
        def calculate_discount(self):
            return self._price * 0.10
        
    class Clothing():
        def calculate_discount(self):
            return self._price * 0.20

class ShoppingCart:
    def __init__(self):
        self._contents = []

    def add_product(self, product):
        self._contents.append({"name": product.name, "price": product.price, "final_price": product.final_price()})

    def remove_product(self, product_name):
        self._contents = [p for p in self._contents if p["name"] != product_name]

    def calculate_total(self):
        return sum(product["final_price"] for product in self._contents)
    
    def list_contents(self):
        return [product["name"] for product in self._contents]

class Order:
    def __init__(self, cart):
        self._cart = cart
        self._total = cart.calculate_total()

    def display_order_summary(self):
        print("Order Summary")
        for product in self._car._contents:
            print(f"-{product['name']}: ${product['final_price']:.2f}")
        print(f"Total: ${self._total:.2f}")


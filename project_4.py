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

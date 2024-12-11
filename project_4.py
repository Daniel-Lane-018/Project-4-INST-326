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
    
    class Electronics(Product):
        def calculate_discount(self):
            return self._price * 0.10
        
    class Clothing(Product):
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

# EXECUTION CODE
class main():
    products = [
        Electronics("Smartphone", 699.99),
        Clothing("Jeans", 49.99),
        Electronics("Laptop", 1199.99),
        Clothing("T-Shirt", 19.99),
        Electronics("Headphones", 199.99),
        Clothing("Jacket", 89.99)
    ]

    cart = ShoppingCart()

    while True:
        print("\nChoose an option:")
        print("1. Add product to cart")
        print("2. View cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_choice = int(input("Enter the product number to add to cart"))
            if 1 <= product_choice <= len(products):
                cart.add_product(products[product_choice - 1])
                print(f"{products[product_choice - 1].name} added to cart.")
            else:
                print("invalid product number")
        elif choice == "2":
            print("\nCart Contents:")
            for product in cart.list_contents():
                print(f"- {product}")
            print(f"Total: ${cart.calculate_total():.2f}")
        elif choice == "3":
            print("\nChecking out...")
            order = Order(cart)
            order.display_order_summary()
            break
        elif choice == "4":
            print("Exiting Program. Have a nice day.")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
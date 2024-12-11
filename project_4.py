class Product:

    def __init__(self, name, price):
        # Initialize product with a name and price
        self._name = name
        self._price = price

    @property
    def name(self):
        # Getter for product name
        return self._name

    @property
    def price(self):
        # Getter for product price
        return self._price

    def calculate_discount(self):
        # discount for a generic product
        return 0

    def final_price(self):
        # final price after applying discount
        return self._price - self.calculate_discount()

class Electronics(Product):
    def calculate_discount(self):
        # 10% discount for electronics
        return self._price * 0.10

class Clothing(Product):
    def calculate_discount(self):
        # 20% discount for clothing
        return self._price * 0.20

class ShoppingCart:
    def __init__(self):
        # Initialize empty shopping cart
        self._contents = []

    def add_product(self, product):
        # Add product to shopping cart
        self._contents.append({"name": product.name, "price": product.price, "final_price": product.final_price()})

    def remove_product(self, product_name):
        # Remove a product from cart by name
        self._contents = [p for p in self._contents if p["name"] != product_name]

    def calculate_total(self):
        # Calculate total cost
        return sum(product["final_price"] for product in self._contents)

    def list_contents(self):
        # List names of products
        return [product["name"] for product in self._contents]

class Order:
    def __init__(self, cart):
        # Initialize order with cart
        self._cart = cart
        self._total = cart.calculate_total()

    def display_order_summary(self):
        # Display summary of order
        print("Order Summary:")
        for product in self._cart._contents:
            print(f"- {product['name']}: ${product['final_price']:.2f}")
        print(f"Total: ${self._total:.2f}")

# EXECUTION CODE

def main():
    # Create products list
    products = [
        Electronics("Smartphone", 699.99),
        Clothing("Jeans", 49.99),
        Electronics("Laptop", 1199.99),
        Clothing("T-Shirt", 19.99),
        Electronics("Headphones", 199.99),
        Clothing("Jacket", 89.99)
    ]

    # Display available products
    print("Available Products:")
    for idx, product in enumerate(products, 1):
        print(f"{idx}. {product.name} - ${product.price:.2f}")

    # Shopping cart
    cart = ShoppingCart()

    while True:
        # Main menu
        print("\nChoose an option:")
        print("1. Add product to cart")
        print("2. View cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add product to cart
            product_choice = int(input("Enter the product number to add to cart: "))
            if 1 <= product_choice <= len(products):
                cart.add_product(products[product_choice - 1])
                print(f"{products[product_choice - 1].name} added to cart.")
            else:
                print("Invalid product number.")
        elif choice == "2":
            # View cart content and total
            print("\nCart Contents:")
            for product in cart.list_contents():
                print(f"- {product}")
            print(f"Total: ${cart.calculate_total():.2f}")
        elif choice == "3":
            # Checkout display order summary
            print("\nChecking out...")
            order = Order(cart)
            order.display_order_summary()
            break
        elif choice == "4":
            # Exit program
            print("Exiting. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
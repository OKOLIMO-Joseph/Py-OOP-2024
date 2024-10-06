class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        #Instance method to display product details
        print(f"Product_Name: {self.product_name}")
        print(f"Price: Shs{self.price:.2f}")
        print(f"Quantity_in_Stock: {self.quantity_in_stock}")

class ShoppingCart:
    # Class variable to track the total number of shopping carts created
    total_carts = 0

    def __init__(self):
        self.items = []  #Array to store products and their quantity
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        #Adds a product to the cart if the quantity.
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} {product.product_name}s to cart.")
        else:
            print(f"The stock is not sufficient {product.product_name}.")

    def remove_from_cart(self, product):
        #Instance variable that removes a product from the cart.
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"You have removed {product.product_name} from cart.")
                return
        print(f"{product.product_name} not found in the cart.")

    def display_cart(self):
        #Instance method to displays all items in the cart
        if not self.items:
            print("The cart is empty")
        else:
            print("My Shopping Cart")
            for product, quantity in self.items:
                print(f"{product.product_name} - Quantity: {quantity}")

    def calculate_total(self):
        #Method to calculate the total amount of the items in the cart
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

#Instances of the classes
if __name__ == "__main__":
    # Examples of the prodcuts
    product1 = Product("Bag", 60000, 7)
    product2 = Product("Shoe", 150000, 4)
    product3 = Product("Watch", 95000, 5)

    # Showing the information about the products in the cart
    product1.display_product_info()
    product2.display_product_info()
    product3.display_product_info()

    # Shopping cart
    cart = ShoppingCart()
    print(sep='\n')

    # Adding products to the cart
    cart.add_to_cart(product1, 3)
    cart.add_to_cart(product2, 2)
    cart.add_to_cart(product3, 4)

    # Showing the prodcuts in the cart
    cart.display_cart()

    # Summationof the total cost
    total_price = cart.calculate_total()
    print(f"Total Price: Shs{total_price}")
    print(sep='\n')

    #Removing the products from the cart
    cart.remove_from_cart(product2)

    # Showing the remaining cart contents
    cart.display_cart()

    # Displaying the total cost after  removing the product
    total_price = cart.calculate_total()
    print(f"Total Price: Shs{total_price}")

class Product:

    #Constructor the product object that takes in the product_name and quantity_in_stock as its arguments
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        
    #Instance method to display the items  in the product list, their names, price and quantity in stock
    def display_product_info(self):
        print('Product Name: ',self.product_name)
        print('Price: ',self.price)
        print('Quantity: ',self.quantity_in_stock) 


class ShoppingCart:
    total_carts = 0

    def __init__(self):
        self.items = []
        ShoppingCart.total_carts +=1

    #instance method to add items to the cart
    def add_to_cart(self, product, quantity):
        self.items.append((product, quantity))
        product.quantity_in_stock -=quantity
        print('You have added', quantity, product.product_name, 'to your cart!')

    #Instance method to remove items from the cart
    def remove_from_cart(self, product):
        item = next(item for item in self.items if item[0] == product)
        self.items.remove(item)
        product.quantity_in_stock += item[1]
        print('You have successfully removed ', product.product_name, 'from the cart')

    #method to display items in the cart
    def display_cart(self):
        if self.items:
            print('My Shopping Cart')
            for product, quantity in self.items:
                print('Selected Product: ', product.product_name, 'Quantity: ', quantity)
        else:
            print('Sorry! Your cart is empty')

    #method to calculate the total cost of items selected
    def calculate_total(self):
        return sum(product.price*quantity for product, quantity in self.items)



pdt_1 = Product('Television', 650000, 65)
pdt_2 = Product('Mattress', 250000, 105)
pdt_3 = Product('Oxford Shoe', 95000, 25)
print('---------Product 1----------')
pdt_1.display_product_info()
print(sep='\n')
print('---------Product 2----------')
pdt_2.display_product_info()
print(sep='\n')
print('---------Product 3----------')
pdt_3.display_product_info()
print(sep='\n')

cart = ShoppingCart()

print('----------Cart-------------')
cart.add_to_cart(pdt_1, 5)
cart.add_to_cart(pdt_2, 2)
cart.add_to_cart(pdt_3, 12)
print(sep='\n')

#Item that have been selected and added to cart
cart.display_cart()

#Displaying the total cost of all the items added to cart
total_price = cart.calculate_total()
print('Total Cost: Shs', total_price)
print(sep='\n')

#IDisplaying the items that have been removed from the cart
cart.remove_from_cart(pdt_3)
#Displaying the remaining items in the cart
cart.display_cart()
#Displaying the cost of the remaining items in the cart
total_price = cart.calculate_total()
print('Total Cost: Shs', total_price)

print('---------THANK YOU!---------')
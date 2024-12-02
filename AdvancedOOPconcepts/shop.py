class ShopItem:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

class Electronics(ShopItem):
    def __init__(self, name, price, stock_quantity, warranty):
        super().__init__(name, price, stock_quantity)
        self.warranty = warranty

    def sell_item(self, quantity):
        r_quantity = self.stock_quantity - quantity
        if r_quantity <= 0: {
            print(f'{self.name} is out of stock')
        }
        else: {
            print(f'Current Quantity of {self.name} in stock: {r_quantity}')
        }

    def item_info(self):
        print(f'Item Name: {self.name}')
        print(f'Price: {self.price}')
        print(f'Warrant: {self.warranty} months')


e1 = Electronics('Phone', 750000, 5, 12)
e1.item_info()
#Selling the item e1
e1.sell_item(5)
print(sep='\n')


e2 = Electronics('Oxford Shoe', 120000, 11, 6)
e2.item_info()

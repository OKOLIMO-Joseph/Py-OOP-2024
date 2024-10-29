class Payment:
    def __init__(self, final_price):
        self.__final_price = final_price

    def get_price(self):
        print(self.__final_price)

    def set_final_price(self, discount):
        self.__final_price = self.__final_price - self.__final_price*(discount/100)

laptop = Payment(700000)
laptop.set_final_price(25)
laptop.get_price()

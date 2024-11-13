from abc import ABC, abstractmethod

class Payment():
    @abstractmethod
    def make_payment(self, amount):
        pass
class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f'Making Card Payment of : {amount}')

class MomoPayment(Payment):
    def make_payment(self, amount):
        print(f'Making Momo Payment of: {amount}')

payment1 = CreditCardPayment()
payment1.make_payment(500)

payment2 = MomoPayment()
payment2.make_payment(600)
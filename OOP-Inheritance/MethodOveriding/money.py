class Payment:
    def __init__(self, amount):
        self.amount = amount

    def paid(self):
        print(f'Paid: {self.amount}')

class cash(Payment):
    def __init__(self, amount):
        super().__init__(amount)

class Momo(Payment):
    def __init__(self, amount, merchantCode):
        super().__init__(amount)
        self.merchantCode = merchantCode

class Visa(Payment):
    def __init__(amount, cvc):
        super().__init__(amount)
        self.cvc = cvc

class Onamanja(Payment):
    def __init__(self, contact, NIN, address, nextOfKin, witness):
        super().__init__(amount)
        self.contact = contact
        self.NIN = NIN
        self.address = address
        self.nextOfKin = nextOfKin
        self.witness = witness
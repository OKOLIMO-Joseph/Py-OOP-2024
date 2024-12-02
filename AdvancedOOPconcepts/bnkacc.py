class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposit: {amount}')

        else:
            print('Invalid deposit')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrawal: {amount}')
        else:
            print(f'Insufficent balance')

    def get_balance(self):
        print(f'Account Balance: {self.__balance}')

jzph = BankAccount('123456789', 'Jzp OKOLIMO', 100000)
jzph.deposit(680000)
jzph.withdraw(390000)
jzph.get_balance()
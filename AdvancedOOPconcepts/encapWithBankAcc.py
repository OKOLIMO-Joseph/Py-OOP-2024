class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully!")
        else:
            print("Invalid withdrawal amount or insufficient balance!")

    def get_balance(self):  # Public method to access the private attribute
        return self.__balance


# Usage
account = BankAccount("123456789", 750)
account.deposit(200)
account.withdraw(100)
print("Current Balance:", account.get_balance())

# Direct access to private attributes will raise an error
# print(account.__balance)  # This will raise an AttributeError

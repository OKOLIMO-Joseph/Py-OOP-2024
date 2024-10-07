class BankAccount:
    # Class variable defining 0.05 interest rate
    interest_rate = 0.05

    def __init__(self, account_holder):
        # Instance variables describing the account(object)
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        #Add new amount to the new balance
        self.balance += amount
        print(f"You have deposited: {amount}")
        print(f'Your New balance: {self.balance}.')

    def withdraw(self, amount):
        #Deposit subtracts the amount from the balance
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Your withdrawal: {amount}")
            print(f'New balance: {self.balance}.')
        else:
            print('You have insufficient balance, Please  make a deposit!')

    def apply_interest(self):
        # Interest is added to the current balance based on the class variable interest_rate
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest of {interest}. Your New balance is {self.balance}.")

    def display_account_info(self):
        #This instance method displays the account holder's name and  the current balance

        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

# Example usage
#Account User 1
print('--------Account User 1---------') # Line to create borders between each user's account details
account = BankAccount("Joseph OKOLIMO")
account.deposit(45000)
account.withdraw(15000)
account.apply_interest()
account.display_account_info()
print('-------------------------------')
print(sep='\n')


#Account User2
print('--------Account User 2---------') # Line to create borders between each user's account details
account = BankAccount("Mukibi Alex")
account.deposit(20000)
account.withdraw(12000)
account.apply_interest()
account.display_account_info()
print('-------------------------------')

class BankAccount:
    def __init__(self,balance=0):
        self.account_balance=balance

    def deposit(self,amount=0):
        self.account_balance+=amount

    def withdraw(self,amount):
        if self.account_balance<amount:
            return False
        self.account_balance-=amount
        return  True

    def display_balance(self):
        print("Current Balance: $%.2f" % self.account_balance)


class BankAccount:
    def __init__(self,balance=0):
        self.account_balance=balance

    def deposit(self,amount=0):
        self.account_balance+=amount

    def withdraw(self,amount=0):
        if self.account_balance<amount:
            return True
        self.account_balance-=amount
        return  False

    def display_balance(self):
        print(" Current Balance: $[{}]".format(self.account_balance))


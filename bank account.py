from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = datetime.now()

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        self.balance -= amount
        return amount

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer name: {self.customer_name}")
        print(f"Account number: {self.account_number}")
        print(f"Date of opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")


# Usage example:
account = BankAccount(account_number=12345, customer_name="George")
print(account.deposit(10000))  # 10000
print(account.check_balance())  # Current balance: 10000
print(account.withdraw(500))  # 500
print(account.check_balance())  # Current balance: 9500
print(account.withdraw(10000))  # Insufficient balance
account.customer_details()

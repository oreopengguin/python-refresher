import numpy


class BankAccount:
    def __init__(self, balance, name, num):
        if not isinstance(balance, float) and not isinstance(balance, int):
            raise TypeError("Balance must be a valid amount of money")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(num, int) and num > 0:
            raise TypeError("Account number must be a positive integer")

        self.balance = balance
        self.name = name
        self.num = num

    def withdraw(self, amnt):
        if not (isinstance(amnt, float) or isinstance(amnt, int)) or amnt < 0:
            raise TypeError("Withdraw amount must be a valid amount of money")
        self.balance -= amnt

    def deposit(self, amnt):
        if not (isinstance(amnt, float) or isinstance(amnt, int)) or amnt < 0:
            raise TypeError("Deposit amount must be a valid amount of money")
        self.balance += amnt

    def display(self):
        return self.name + f"'s account has a balance of ${self.balance}"

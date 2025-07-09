class BankAccount:
    def __init__(self, balance: int | float, name: str, num: int):
        """
        Initializes the bank account with the users balance, name, and account number
        """
        if (
            not isinstance(balance, float)
            and not isinstance(balance, int)
            and balance > 0
        ):
            raise TypeError("Balance must be a valid amount of money")
            # return False
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
            # return False
        if not isinstance(num, int) and num > 0:
            raise TypeError("Account number must be a positive integer")
            # return False

        self.balance = balance
        self.name = name
        self.num = num
        # return True

    def withdraw(self, amnt):
        """
        Withdraws a passed amount of money by subtracting it from the balance
        @param amnt the amount of money to subtract
        @ret True if money is successfully withdrawed, False if it can't be 
        """
        if not (isinstance(amnt, float) or isinstance(amnt, int)) or amnt < 0:
            # raise TypeError("Withdraw amount must be a valid amount of money")
            print("Withdraw amount must be a valid amount of money")
            return False
        if self.balance - amnt < 0:
            # raise ValueError("Insufficient balance")
            print ("Insufficient balance")
            return False
        self.balance -= amnt
        return True

    def deposit(self, amnt):
        """
        Deposits a passed amount of money by adding it to the balance
        @param amnt the amount of money to add
        @ret True if money is successfully deposited, False if it can't be
        """
        if not (isinstance(amnt, float) or isinstance(amnt, int)) or amnt < 0:
            # raise TypeError("Deposit amount must be a valid amount of money")
            return False
        self.balance += amnt
        return True

    def display(self):
        """
        Displays the account owner's name and their balance
        """
        return self.name + f"'s account has a balance of ${self.balance}"

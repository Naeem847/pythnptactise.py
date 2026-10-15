
class BankAccount:
    # 1. Constructor
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance  # Private attribute
        self.transactions = []    # Transaction history

    # 2. Encapsulation: read-only balance
    @property
    def balance(self):
        return self.__balance

    # 3. Deposit method
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero!")
        else:
            self.__balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print(f"Deposit successful! Balance: {self.__balance}")

    # 4. Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
        elif amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Withdrawal successful! Balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    # 5. Check balance
    def check_balance(self):
        print(f"Account holder: {self.name}")
        print(f"Current balance: {self.__balance}")

    # 6. Display transaction history
    def show_history(self):
        print("\nTransaction History:")

        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


# 7. Create an object

account = BankAccount("Naeem", 500)

account = BankAccount("Naeem", 500)

# 8. Call methods

account.check_balance()
account.deposit(1000)
account.withdraw(300)
account.withdraw(2000)
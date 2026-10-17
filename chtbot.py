
from datetime import datetime, date


class BankAccount:
    # Automatically generate account numbers
    next_account_number = 1001

    def __init__(self, name, balance=0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.name = name
        self.__balance = balance
        self.account_number = f"ACC{BankAccount.next_account_number}"
        BankAccount.next_account_number += 1

        self.transactions = []
        self.is_active = True

        # Daily withdrawal limit
        self.daily_limit = 5000
        self.daily_withdrawn = 0
        self.withdrawal_date = date.today()

    # 1. Read-only balance
    @property
    def balance(self):
        return self.__balance

    # 2. Record transaction with date and time
    def record_transaction(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{time} | {message}")

    # 3. Check whether account is active
    def check_active(self):
        if not self.is_active:
            print("Account is closed. Transaction not allowed.")
            return False
        return True

    # 4. Deposit money
    def deposit(self, amount):
        if not self.check_active():
            return

        if amount <= 0:
            print("Deposit amount must be greater than zero!")
            return

        self.__balance += amount
        self.record_transaction(f"Deposited: Rs. {amount:.2f}")
        print(f"Deposit successful! Balance: Rs. {self.__balance:.2f}")

    # 5. Withdraw money with daily limit
    def withdraw(self, amount):
        if not self.check_active():
            return

        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
            return

        # Reset daily withdrawal amount on a new day
        today = date.today()
        if today != self.withdrawal_date:
            self.daily_withdrawn = 0
            self.withdrawal_date = today

        if amount > self.__balance:
            print("Insufficient funds!")
            return

        if self.daily_withdrawn + amount > self.daily_limit:
            remaining = self.daily_limit - self.daily_withdrawn
            print(f"Daily limit exceeded! Remaining limit: Rs. {remaining:.2f}")
            return

        self.__balance -= amount
        self.daily_withdrawn += amount

        self.record_transaction(f"Withdrawn: Rs. {amount:.2f}")
        print(f"Withdrawal successful! Balance: Rs. {self.__balance:.2f}")

    # 6. Transfer money to another account
    def transfer(self, other_account, amount):
        if not self.check_active():
            return

        if not other_account.check_active():
            return

        if self is other_account:
            print("Cannot transfer money to the same account!")
            return

        if amount <= 0:
            print("Transfer amount must be greater than zero!")
            return

        if amount > self.__balance:
            print("Insufficient funds for transfer!")
            return

        self.__balance -= amount
        other_account._BankAccount__balance += amount

        self.record_transaction(
            f"Transferred Rs. {amount:.2f} to {other_account.account_number}"
        )
        other_account.record_transaction(
            f"Received Rs. {amount:.2f} from {self.account_number}"
        )

        print("Transfer successful!")
        print(f"Your balance: Rs. {self.__balance:.2f}")

    # 7. Check balance
    def check_balance(self):
        if not self.check_active():
            return

        print(f"Account holder: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Current balance: Rs. {self.__balance:.2f}")

    # 8. Display account details
    def account_details(self):
        print("\n----- ACCOUNT DETAILS -----")
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: Rs. {self.__balance:.2f}")
        print(f"Daily withdrawal limit: Rs. {self.daily_limit:.2f}")
        print(f"Account status: {'Active' if self.is_active else 'Closed'}")

    # 9. Change account holder name
    def change_name(self, new_name):
        if not self.check_active():
            return

        new_name = new_name.strip()

        if not new_name:
            print("Name cannot be empty!")
            return

        old_name = self.name
        self.name = new_name
        self.record_transaction(f"Name changed from {old_name} to {new_name}")
        print(f"Account holder name updated to {self.name}")

    # 10. Show transaction history
    def show_history(self):
        print("\n----- TRANSACTION HISTORY -----")

        if not self.transactions:
            
            print("No transactions yet.")
            return

        for transaction in self.transactions:
            print(transaction)

    def receipt(self):
        print("\n----- ACCOUNT RECEIPT -----")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Account holder: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Current balance: Rs. {self.__balance:.2f}")
        print("----------------------------")

    # 12. Close account if balance is zero
    def close_account(self):
        if not self.check_active():
            return

        if self.__balance != 0:
            print("Please withdraw or transfer the remaining balance first.")
            return

        self.is_active = False
        self.record_transaction("Account closed")
        print("Account closed successfully!")




account1 = BankAccount("Naeem", 5000)
account2 = BankAccount("Ali", 2000)

# Display account details
account1.account_details()

# Deposit money
account1.deposit(1000)

# Withdraw money
account1.withdraw(500)

# Transfer money to another account
account1.transfer(account2, 1000)

# Check balances
print("\nAccount 1:")
account1.check_balance()

print("\nAccount 2:")
account2.check_balance()

# Change account holder name
account1.change_name("Muhammad Naeem")

# Print receipt
account1.receipt()

# Display transaction history
account1.show_history()
account2.show_history()

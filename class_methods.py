class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_marks(self):
        print("Student:", self.name)
        for mark in self.marks:
            print(mark)
obj = Student("Ali", [80, 85, 90])
obj.show_marks()

# practice oop concepts
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_average(self):
        average = sum(self.marks) / len(self.marks)
        print("Student:", self.name)
        print("Average Marks:", average)


obj = Student("Ali", [80, 85, 90])
obj.show_average()

# Example 3: Bank Account

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


obj = BankAccount("Ali", 5000)

obj.show_balance()

obj.deposit(2000)

obj.withdraw(1500)

obj.show_balance()
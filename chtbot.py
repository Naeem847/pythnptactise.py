class Bankaccount:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        
        if amount<=self.balance:
            self.__balance-=amount
            print(f"withdrawal successful!!! your current balance is {self.balance}")
        else:
            print("insufficient funds")

account=Bankaccount(500)  
account.withdraw(500)       
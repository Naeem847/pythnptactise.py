class Animal:
    def __init__(self):
        self.name="animal"
        self.eat="food"
    def show(self):
        print(f"name: {self.name}, eats: {self.eat}")  

class dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "dog"
        self.eat = "meat"

    def show(self):
        print(f"name: {self.name}, eats: {self.eat}")
class cat(Animal):
    def __init__(self):
        super().__init__()
        self.name = "cat"
        self.eat = "fish"
    def show(self):
            print(f"name: {self.name}, eats: {self.eat}")
a=Animal()
b=dog()
c=cat()
a.show()
b.show()
c.show()
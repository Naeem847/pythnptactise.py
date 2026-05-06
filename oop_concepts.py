class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Polymorphism in action
for obj in [Dog(), Cat()]:
    obj.sound()
#   2nd example of polimorphism
class Animal:
    def sound(self):
        print("Animal make sounds")

class Dog(Animal):
    def sound(self):
        print("dog barks")

class cat(Animal):
    def sound(self):
        print("cat meaws")

animal=[Dog(),cat()]

for a in animal:
    a.sound()


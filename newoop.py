class Dog:
    def sound(self):
        return "Dog barks"

class Cat:
    def sound(self):
        return "Cat meows"

class Cow:
    def sound(self):
        return "Cow moos"

def animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
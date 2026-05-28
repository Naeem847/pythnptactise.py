class Car:

    def __init__(self, brand):
        self.brand = brand

cars = [
    Car("Toyota"),
    Car("Honda"),
    Car("BMW")
]

for car in cars:
    print(car.brand)
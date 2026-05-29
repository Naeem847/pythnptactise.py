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
# if else condition statement
trafic_light = "red"
if trafic_light=="green":
    print("you can go")
else:
    print("you must stop")

# if else if condition statement using user input
user=input("enter your light color: ")

if user=="green":
    print("you can go")
elif user=="yellow":
    print("you should be ready to stop")
else:
    print("you must stop")
    # if else if condition statement
car_speed=60
seat_belt=True
if car_speed<=60:
    if seat_belt:
        print("you are safe")
    else:
        print("please wear your seat belt:")
else:
    print("slow down, you are exceeding the speed limit:")   

# 4. Logical Operators in Conditional Statements
pedestrian_signal = "walk"

is_flashing = False

if pedestrian_signal == "walk" and not is_flashing:

    print("Pedestrian can cross safely")
else:
    print("Pedestrian should wait")

# OR Operator

traffic_light = "red"

vehicle_type = "ambulance"

if traffic_light == "green" or vehicle_type == "ambulance":

    print("You can go")
else:
    print("You must stop")

# NOT Operator
pedestrian_signal ="don't walk"

if not pedestrian_signal == "walk":

    print("Do not cross")
else:
    print("You can cross")    
 
# 5. Case Sensitivity in Conditions
traffic_light = "Red"
if traffic_light == "red":
    print("You must stop")
else:
    print("Slow down and prepare to stop")
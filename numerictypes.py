num1=12
num2=12.1
num3=0
print("num1:",type(num1))
print("num1:",type(num2))
print("num1:",type(num3))
# 
a = 1000
b = 1000
print(a is b)
# cancatinnation of the variables
name1="ali"
name2="hassan"
full_name=name1+" "+name2
print(full_name)
# formatted string
name="naeem"
age=12
print(f"my name is {name} and my age is {age}")

a = 10
# instance variable
print(isinstance(a, int))   # True
print(isinstance(a, float)) # False
# boolean type in python 
is_python_easy=True
is_coofee=False
print("ispython is true:",type(is_python_easy))
print("is_coofee is false:",type(is_coofee))
# boolean check using the loop
if is_python_easy:
    print("yes python is easy!")
# creating list in different ways
num1=[]
numbers=[1,2,3]
mixed_data=["ali",2.45,True]
print("this is empty list:",type(num1))
print("this is numbers list:",type(numbers))
print("this is mixed_list:",type(mixed_data))
# Accessing index by elements in list
first_name=numbers[0]
last_name=numbers[-1]
print(first_name)
print(last_name)
# adding elements in list append,insert,pop and remove
numbers.append(50)
print(numbers)
numbers.insert(1,50)
print(numbers)
remove_item=numbers.pop()
print(numbers)
numbers.remove(1)
print(numbers)
numbers[2]=34
print(numbers)
# tuppels in python
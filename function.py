# add two numbers for practise.
# num1=int(input("enter the num 1:"))
# num2=int(input("enter the num 2:"))
def add(num1,num2):
    print("number1:",num1)
    print("number2:",num2)
    result=num1+num2
    print("addition of two num is:",result)
    
result=add(3,4)
print("result",result) 
# default argument
def greet(name="john"):
    print(f"hello {name}")
greet() 
greet("alice")
# keyword argument in python:
def greet(f_name,l_name):
    print(f"hello{f_name},{l_name}")  
greet(f_name="java",l_name="python")   
print(greet)  
print(("location of the greet is:",id(greet)))
# variable lenght arguments
def greet(*names):
    for name in names:
     print(f"hello,{name}")
greet("c++","jaca","c#")
# return vs print in functions
# print in function:
def greet():
    print("hello python")
greet()  
# return in function
def greet():
    return"hello python"
message=greet()
print(message)
# basic function with return:
def add(num1,num2):
    return num1+num2
result =add(4,6)
print("sum of two num is:",result)
# function with default paremeters
def full_name(f_name="joe",l_name="willson"):
    print(f"full_name:{f_name},{l_name}")
full_name() # use default value
full_name("jackson") #override the f_name



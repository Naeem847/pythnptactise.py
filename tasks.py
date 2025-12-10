#Task 1:
print("wellcome to artificial intelligence Lab:")
name="Ai student"
age=22
marks=[85,90,78]
student={"name":name,"age":age,"marks":marks}
print(student)
#Task 2:
for i in range(1,6):
    if i%2==0:
        print(i,"is even")
    else:
        print("odd") 
#Task 3:   
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("factorial of 5:",factorial(5))
#Task 4:
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print("name:", self.name)
        print("rollno:", self.rollno)
s1 = student("ali", 101)
s1.display()
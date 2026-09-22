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
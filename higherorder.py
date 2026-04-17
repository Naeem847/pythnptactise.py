# # use map() to apply a function to each item in a list
def double(x):
    return x * 2
number=[1,2,3,4,5]
double= list(map(double, number))
print(double)
# # Output: [2, 4, 6, 8, 10]
# # use filter() to filter items in a list based on a condition
numbers = [1, 2, 3, 4, 5, 6]
def is_even(n):
    return n % 2 == 0
result = list(filter(is_even, numbers))
print(result)

# use reduce() to apply a function cumulatively to the items of a list
from functools import reduce
def add(x, y):
    return x + y
numbers = [1, 2, 3, 4, 5] 

total = reduce(add, numbers)
print(total)
# # use zip() to combine two lists into a list of tuples
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

result = list(zip(names, ages))
print(result)
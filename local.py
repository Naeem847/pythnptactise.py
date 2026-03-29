# this code defines a  function outer function and inner function.
def outerfunc():
    def innerfunc():
        return "hello from innerfunc"
    return innerfunc()
print(outerfunc())
#using outer func and also call the inner func
def outerfunc():
    x=10
    def innerfunc():
        return x
    return innerfunc
f=outerfunc()
print(f())
# using closure to create a multiplier function that takes a number n and returns a function that multiplies its input by n.
def multiplier(n):
    def innerfunc(x):
        return x*n
    return innerfunc
double=multiplier(2)
triple=multiplier(3)
print(double(5))
print(triple(5))
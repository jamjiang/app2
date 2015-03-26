__author__ = 'jamjiang'
def sayHello():
    print'Hello World!'#block belonging to the function
x=50
print id(x)
def func(x):
    print'x is',x
    x=2
    print id(x)
    print'changed local x to',x
func(x)
print id(x)
print'x is still',x

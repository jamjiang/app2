__author__ = 'jamjiang'
x = 50
print id(50)
def func():
    global x
    global y
    print 'x is', x
    x = 2
    print id(x)
    y = 3
    print 'Changed global x to', x
func()
print'Value of x is', x
print(y)
print id(x)
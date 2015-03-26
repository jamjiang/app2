__author__ = 'jamjiang'
class Person:
    def __init__(self, name):
            self.name = name
    def sayHi(self):
        print 'hi!, I am', self.name

david = Person('David')
david.sayHi()

Person('leo').sayHi()


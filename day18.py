'''
Polymorphism
------------
--->This means "many forms" . it allows the same function,method,or operator to
    behave differently depending on the object...

1.Method overloading
--->Method overloading means defining multipl methods with the same name but
    different parameters

#1
class calculator:
    def add(self,a,b,c=5):
        return a+b+c
an=calculator()
print(an.add(23,7,))
print(an.add(23,7,55))

#2
class calc:
    def add(self,a,b):
        return a+b
    def add (self,a,b,c=0):
        return a+b+c
an=calc()
print(an.add(22,22))

2.Method overriding
--->This occurs when a child class provides its own implementation of a method
    already defined in the parent clas.....


class animal:
    def sound(self):
        print("Animal makes sound")

class dog(animal):
    def sound(self):
        
        print("Dog Barks")

obj=dog()
obj.sound()

To access the parent class method inside a child class, use super().
class animal:
    def sound(self):
        print("Animal makes sound")

class dog(animal):
    def sound(self):
        super().sound()
        print("Dog Barks")

obj=dog()


3.Operating overloading
------------------------

--->This allows operators such as +,-,* etc, to perform different actions for user-defined objs

class

note:
--->The operator inside the method will overload a special method or operator given 
ex:

class stu_:
    def __init__(self,marks):
        self.marks=marks
    def __add__ (self,other):
        return self.marks+other.marks
so_1=stu_(4)
so=stu_(55)

print(so_1+so)


Data abstraction
--> This is the process of hiding internal implementation details and showing only essential
    features to the user
--->it focuses on what an object does rather than how it does it....


'''

from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class rec(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimeters(self):
        return 2*(self.a*self.b)
an=rec()
print(an.area())




























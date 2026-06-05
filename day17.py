'''
Inheritance
-----------
--->this allows one class to aquire the properties and methods of another class
----------------------------------------------------------------------
Types
------
1.Single Inheritance
---> A class inherts from a single parent class

ex:
class father:
    def land(self):
       `     ``     print("my father have 5Acer")
class charan(father):
    def my_own(self):
        print("I have 2acer")

prop=charan()
prop.land()
----------------------------------------------------------------------
2.multiple Inheritance

--->a child class can have multiple base (parent) classes instead of just one.

ex:
class Father:
    def land(self):
        print("My father have 5 acers")
class mother:
    def gold(self):
            print("My Mother have 10gms gold")
class charan(Father,mother):
    def mine(self):
            print("I have ntg")

prop=charan()
prop.land()
prop.gold()
-----------------------------------------------------------------------
3.Multi-level Inheritance
--->A class inherits from a parent class and mother class inherits from that child class
ex:
class grandfather:
    def land(self):
        print("My grandfather have 5 acers of land")
class father(grandfather):
    def flat(self):
        print("My father have 1 flat at vizag")
class son(father):
    def ntg(self):
        print("I have both 5 acers and i flat at vizag")
all=son()
all.land()
all.flat()
all.ntg()
-----------------------------------------------------------------------
4.Hierarchical Inheritance
------------------------------
--->Multiple child classes inherts from a single parent

class father:
    def land(self):
        print("Have 10 acers of land")

class charan(father):
    def mine(self):
        print("Job")
class sai(father):
    def bros(self):
        print("Jobless")

distu=sai()
distu.bros()
distu.land()

so=charan()
so.mine()
-----------------------------------------------------------------------

5.Hybrid Inheritance
--->This is the combination of two or more types of Inheritance
class A:
    def some(self):
        print("class A")
class B(A):
    def sums(self):
        print("class B")
class c(A):
    def sems(self):
        print("class C")
class D(B,c):
    def so(self):
        print("class D")

form=D()
form.so()
form.some()
form.sums()
form.sems()


-----------------------------------------------------------------------

class Father:
    def land(self):
        print("My father have 5 acers")
class mother:
    def gold(self):
            print("My Mother have 10gms gold")
class charan(Father,mother):
    def mine(self):
            print("I have ntg")

prop=charan()
prop.land()
prop.gold()



class grandfather:
    def land(self):
        print("My grandfather have 5 acers of land")
class father(grandfather):
    def flat(self):
        print("My father have 1 flat at vizag")
class son(father):
    def ntg(self):
        print("I have both 5 acers and i flat at vizag")
all=son()
all.land()
all.flat()
all.ntg()


class sachin:
    def cent(self):
        print("Sachin scored 100 centuries")
class virat(sachin):
    def centu(self):
        print("Virat scored 82 centuires")

most=virat()
most.cent()
most.centu()


class A:
    def methodA(self):
        print("From A")
class B:
    def methodB(self):
        print("From B")

class C(A, B): 
    pass

obj = C()
obj.methodA()  
obj.methodB() 


class father:
    def land(self):
        print("Have 10 acers of land")

class charan(father):
    def mine(self):
        print("Job")
class sai(father):
    def bros(self):
        print("Jobless")

distu=sai()
distu.bros()
distu.land()

so=charan()
so.mine()


class A:
    def some(self):
        print("class A")
class B(A):
    def sums(self):
        print("class B")
class c(A):
    def sems(self):
        print("class C")
class D(B,c):
    def so(self):
        print("class D")

form=D()
form.so()
form.some()
form.sums()
form.sems()

Super()methods
------------------
--->Super() is used to access methods and constructor of the parent class from the child class


class parent:
    def display(self):
        print("Method Parent")
class child(parent):
    def display(self):
        super().display()
        print("Method Child")

any_=child()
any_.display()

'''

class person:
    def __init__(self,name):
        self.name=name
class stu_(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def show(self):
        print(f"Name :{self.name}")
        print(f"Roll No:{self.roll}")
any_=stu_("Sai",1)
any_.show()













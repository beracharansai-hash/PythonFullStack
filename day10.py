'''
assert
-----------
--->This is debugging statement used to test whether the
    condition is true.

    ex:
        num=10
        assert num>15
        print("True')

Functions()
-----------
>A Function is a block of code which only execute when it is called
>you can pass data,known as parameters into a function.
>To avoid repeated lines in code

---> def function_name(parameters):
              --------
              --------
function_name(arguments)

ways to pass arguments:
1.Required Argument
--->Required arguments are the parameters that must be given
    when calling a function.
num=9
def even(num,num_2):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

even(109,100)

2:Default arguments:
--->Default arguments already have a value assigned in the
    function definition.
    If the user does not pass a value, the default value is used.

def even(name="Teja",age=89,sal=10):
    print(name)
    print(age)
    print(sal)
even("bhanu",88,75000)




keyword arguments
-----------------
--->We can send arguments with key=value syantax.By this, the
    order of argumentsdoes not matter

def even(age,sal,name):
    print(name)
    print(age)
    print(sal)
even(name="charan",age=22,sal=46000)


variable length arguments
-------------------
Adding a star(*) before the parameters name in the function,
receive a tuple of arguments and can access items with indexes

def even(*name):
    print(name)
even("charan","sai")



name="teja"
def even(any):
    print(any)
even(name)



for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

def add(num1,num2):
    print(num1+num2)
add(33,300)






for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


print()



add(400,300)


def name(*names):
    print(names)
name("Sai","charan","Sampath")

'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
for number in range(1, 101):
    if is_prime(number):
        print(number, end=" ")









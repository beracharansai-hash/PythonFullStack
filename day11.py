'''
Built in function
------------------
print()
input()
len()
type()
max()
min()

m=[3,4,1,2]
print(sorted(m))
print(m)
(Note:Not permenently sorted)
----------------
m=[3,4,1,2]
m.sort()
print(m)
(This is permenently sorted)

----------------------------------------------------------

Recursive function
-----> A Recursive Function that calls itself to solve a
problem by breaking into a small or simple sub-problems

----------------------------------------------------------


def fac(num):
    if num==1:
        return 1
    return num*fac(num-1)
print(fac(5))

def prime_num(num):
    if num>2:
        return False
    for i in range(2,num+1):
        if num%i==0:
            return False
    return True
    for i in range(1,num+1):
        if prime_num(num):
            print(num,end=" ")
prime_num(55)


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
------------------------------------------------------------
return()this ends a function execution and sends a value back
to the code that called the function
ex:

def add(a,b):
    return a+b
res=add(4,5)
print(res)

Lambda functions
----------------------
---> A lambda function is a small anonamus functions
---> lambda can take "n" number of arguments,but only one
     expression
syntax----> lambda arguments:expression

so=lambda a,b,c: a+b+c+a
print(so(3,4,9))

sa=lambda a,b,c:a*b*c*a
print(sa(5,4,7))

su=lambda a,b,c:a-b-c-a
print(su(10,2,4))

'''

def prime(num):
    if num<=1:
        print("Not Prime")
        return
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prime")
prime(17)

def even(


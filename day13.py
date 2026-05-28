'''
List comprehension
------------------
--->Lc offers a shortest syntax when we want to create a new
    list from existing list
Syntax--->vari_name=[expression loop condition]

old_=[1,2,3,4,5]
new_=[so for so in old_ if so%2==0]
print(new_)


old_=[1,2,3,4,5]
new_=[so if so%2!=0 else "even" for so in old_]
print(new_)


Generators
-----------
--->generators in python are a special type of itterable,allowing
    users to iterate over data efficiently without storing
    everything in memory..
--->they generate values lazily using yeild keyword

Why to use Generators?
#Generators does not store the entire data set in the memory they
generate values on the fly
#Avoid unnecessary storage of data speed up execution


How it works
-------------
-->it looks like normal function but uses the yield keyword insted
of return
-->when the function is called, it does not execute immediately.
insted,it return a generator object which can be iterated using
loop or next() function

def simple_gen():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("end")
gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))



def any(num):
    for i in range(num):
        yield i*i
a=any(5)
print(next(a))
print(next(a))
print(next(a))


def squ(num):
    result=[]
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(squ(5))


def fibonacci():
    n = int(input("Enter limit: "))
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
fibonacci()



count=0
so="all live cricket streaming, live scores, ball-by-ball "
any=''
for j in so:
    if j  in "AEIOUaeiou":
        any+=j
        count+=1
print(any)
print(count)
    



























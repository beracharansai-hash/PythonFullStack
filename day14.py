'''

modules
----------
---> a module in python is a file that contains python code such as
-Variables
-functions
-classes
-ststements

two types sof modules
---------------------
user-defined
build-in

def add(a,b):
    return a+b
def sub(a-b):
    return a-b


import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2,5))

import os
os.remove("modules.py")


import modules
print(modules.add(4,6))

from math import sqrt
print(sqrt(25))

from math import pow
print(pow(2,5))


import sys
print(sys.version)

import os
os.mkdir("Sampathhh.py")
os.rmdir("Sampathhh.py")


import random
print(random.randint(1000,9999))



from collections import Counter
data=['a','b','c','d','d']
counter=Counter(data)
print(counter)
'''
from collections import defaultdict
dd= defaultdict(int)
dd['missing']+=1
print(dd['missing'])
print(dd)



















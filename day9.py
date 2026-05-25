
'''
for i in range(1,10):
    for j in range(1,2):
        print(i)
        print(j



num=9
for j in range(1,11):
    print(f"{num}x {j}={num*j}")



so=input("Enter the word")
empty_str=""
for j in so:
    empty_str=j+empty_str
    print(empty_str)
if empty_str==so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not a pali")

#armstrong number
num=int(input("Enter the value"))
s=0
leng=len(str(num))
for i in str(num):
    s+=int(i)**leng
if s==num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")

#perfect number
num=28
per_num=0
for j in range(1,num):
    if num%j==0:
        per_num=+j
if per_num==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} not a perfect number")

#prime number
num=129
count=0
for k in range(1,num+1):
    if num%k==0:
        count+=1
if count==2:
    print(f"{num}is a prime number")
else:
    print(f"{num} is not a prime number")

#stars

star_=5
for g in range(1,star_+1):
    for d in range(1,g+1):
        print("*",end="")
    print()

#


star=5
count=0
for g in range(1,star+1):
    for d in range(1,g+1):
        count+=1
        print(d, end ="")
    print()




num=5
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()


num=10
for i in range(1,num+1):
    if i!=2:
        for j in range(1,i+1):
            print(j,end="")

    print()



star = int(input("Enter the number: "))

for i in range(1, star+1):
    count = 0
    if i != 2:    
        for j in range(1, i+1):
            count += 1
            print(count, end=" ")
        print()




star = int(input("Enter the values: "))

for i in range(1, star+1):
    for j in range(1, i+1):
        print(chr(64+j), end=" ")
    print()


num=5
for j in range(1,num+1):
    print(""*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()
     

rows = 5

for i in range(rows):
    if i <= 2:
        stars = i + 1
    else:
        stars = rows - i
    for j in range(stars):
        print("*", end="  ")

    print()

'''
rows = 3
for i in range(rows):
    for j in range(rows):
        if (i == 0 and j == 1) or \
           (i == 1 and (j == 0 or j == 2)) or \
           (i == 2 and j == 1):
            print("*", end="")
        else:
            print(" ", end="")

    print()














    
        

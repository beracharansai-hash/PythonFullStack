'''
a=0
b=1
def finaaci(a,b):
    limit_=int(input("Enter the Input"))
    print(a,b,end=" ")
    for i in range(1,limit_):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
finaaci(a,b)
    
Remove duplicates from the list


a=[2,5,7,9,2,7]
b=[]
def dupli(a,b):
    for j in a:
        if j not in b:
            b.append(j)
    print(b)
dupli(a,b)
        
#count the words in the string

a="Please paste your text"
a.split()
print(len(a))

'''
count=0
a=input().split()
def count_(a,count):
    for j in a:
        count+=1
        print(count)
count_(a,count)





#1.Program to convert 24h clock into normal
'''
time_=input("enter 24 hours time:")
parts_=time_.split(":")
hour_=int(parts_[0])
min_=int(parts_[1])
print(f"{time_}is converted into {hour_-12}:{min_}PM")

List--------
--->list is a collection of different datatype
--->[] and seperated by ,
--->mutable

methods
----------
append()
----------
--->This method is used to add new items into list,and it will be in the last item in the list

any=[1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4]]
print(any[2][4])
-->append is mutable
---> can able to modify the particular variable

any=[1,2,3]
any.append(6)
print(any)
any.append(22)
print(any)

----------------
----------------
extend()
-------
--->This method is used to add itterable into list
    ,and it will in the last index position,each value or substring
    is each index in the lsit

Syntax--->variable_name.extend(itterable)


string is immutable
--->cannot able to modify the variable
so="python is a "
print(so.replace("python","java"))
print(so)

pop()
--------------
used to remove the item from the list,but will mention here
index position in the pop method
 syntax------->variable_name.pop(index position)
any=[1,2,3]
any.pop(0)
(here o index position will be removed)
------------------

remove()
------------------
--->used to remove the item from the list,but will
    mention here direct in the remove method

any=[1,2,3,4]
any.remove(2)
print(any)


so=["python",2,3,"java"]
so.remove("python")
print(so)







'''
Sets
-------
------>A set is an unordered collection of unique elements.
       It is a built-in data type commonly used for removing duplicates
------> Duplicate valuess are not allowed
------> items are not stored in index order
------> {}

a={1,2,2,3,41}
b={62,23,42,51}
print(a,b)
----------
methods
----------
union()
------> It will Give all values from 2 sets together in once.
------>variable_name.Union(another variable)
a={1,2,2,3,41}
b={62,23,42,51}
print(a|b)
--------------

intersection()
------> To get the common elements from both the sets
------>syntax---> variable_name.intersection(another variable)

a={1,2,2,3,41}
b={62,23,42,2,51}
print(a and b)
print(a.intersection(b))

-------------------
difference()
-------------------

----> to get the difference values from the set
syntax-----> variable_name.difference(anaother variable)


a={1,2,2,3,41,5,7,8}
b={62,23,42,2,51,1,2,3,4}
print(a - b)
print(a.difference(b))


#symmetric difference
a={1,2,3,4,5,6}
b={62,23,42,2,51,1,2,3,4}
print(a-b)
print(a.symmetric_difference(b))


add()
---------
-----> to add new elements in the list
syntax: variable_name.add(element)
any={1,2,2,3,4}
any.add(41)
print(any)

----------
Update()
----------
----> to add multiple elements into the set
syntax---> variable_name.update([elements])

any={1,2,3,3,4,5}
any.update([8,7,9])
print(any)

-----------
remove()
-----> used to remove values or elements from the set.
but it will throw error if element is not found.

any={1,2,3,3,4,5}
any.remove(2)
print(any

Discard()
-------->used to remove values or elements from the set.
and it will not throw error if the element is not found.



















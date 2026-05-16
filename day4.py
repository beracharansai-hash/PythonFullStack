
'''
-------------------

CONCATINATION
-------------------
--->THE(+)FOR INT AND CAN ADD , BUT FOR THE OTHER DATA TYPES
IT WILL ACT AS CONCATINATING THE DATA TYPES


tuple
------------------
---> COLLECTION OF DIFFERENT DATA TYPES SEPERATED BY COMMAS, REPRESENTED IN
() AND IMMUTABLE

------------------

count()
--->this used to count the particular item in the tuple

syntax--->variable_name.count(item)


some=(1,"python",[1,2],(3,4),"python")
print(some.count("python"))

------------------

inddex()

------------------
----> used to find out the index position of the item,
    and only gives the first occurance



some=(1,[1,2],"python")
print(some.index("python"))

any=(1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4])
print(any[4])



Dictionary

----------------
---> Dict is a key : value pair, key and value is seperated by: and
    pair is seperated by comma ","

-----> represented by {}

syntax-----> dict()
----------------

methods

----------------
keys()
----------------
--->used to get all the keys from the dict
syntax---->  dict.keys()

values()
---------------
---> used to all the values of keys from the dict
syntax----> dict.values()




charan_details={"name":"charan",
              "age":22,
              "ph_num":999999999,
              "aadh_num":888888}
print(charan_details)
print(charan_details.keys())
print(charan_details.values())


charan_details={"name":"charan",
              "age":22,
              "ph_num":999999999,
              "aadh_num":888888}
print(charan_details)
print(charan_details["name"])

update()
-----> used to add a new "key:value" pair to the dictinory 
--------------


charan_details={"name":"charan",
              "age":22,
              "ph_num":999999999,
              "aadh_num":888888}
print(charan_details)
print(charan_details.keys())
print(charan_details.values())

charan_details.update({"pan_num":99998888888})
charan_details["name"]="Sai"
charan_details["aadh_num"]="233333545343"
print(charan_details)

clear()
-> used to remove all the items in the dicty









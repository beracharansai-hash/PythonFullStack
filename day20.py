'''
Regular Expression (RegEx)
--->RegEx is a sequence of char that form a searching patterns
--->This can be used to check if a string contain the specified search pattern
--->Python has a built in package called 're' which can be used to work with RegEx

Functions in re
---------------
.findall
.search
.fullmatch

Metachar
--------
[]---> a-z,A-Z,0-9 AND ANY SPECIFIED SEQUENCE.
.--->HERE EACH DOT IS ONE CHAR
^-->This look for the,string is starting with specified sequence or not
$--->This look for the,string is ending with specified sequnce or not
*--->Zero or more
?--->Zero or one
+---> one or more
{}--->


special sequence
----------------
\S---> No Space
\s---> Only spaces
\D---> non-digits
\d---> only-digits
\w---> consider alphabet numbers and _
\W---> Gives special characters(Non-Words)

import re
any="elow or click Help above for more information."
print(re.findall('\S',any))


'''

import re
mobile=input("Enter 10 digit number :")
any_=re.fullmatch('[6-9][0-9]{9}',mobile)
if any_:
    print(f"{mobile} this is inidan number")
elif re.fullmatch('0[0-9]{10}',mobile):
    print("It is a Landline number")

else:
    print(f"{mobile} this is not indian number")





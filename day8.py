'''
elif:

--------------------------------------------------------------
stu_name=input("Enter the Student Name :")
stu_marks=int(input("Enter the Marks :"))
if stu_marks>=90:
    print("A+")
elif stu_marks>=80:
    print("A")
elif stu_marks>=70:
    print("B+")
elif stu_marks>=60:
    print("B")
elif stu_marks>=50:
    print("c+")
elif stu_marks>=35:
    print("pass")
else:
    print("fail")
--------------------------------------------------------------
a=int(input("Enter the value : "))
b=int(input("Enter the value : "))
c=int(input("Enter the value : "))
if a>b and a>c:
    print(f"{a} is greater than {b} and {c}")
elif b>a and b>c:
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")

--------------------------------------------------------------

SBI_bank={"ATM PIN":"6000"}
pin=input("Enter 4 digit ATM pin:")
if len(str(pin))==4:
    if pin in SBI_bank["ATM PIN"]:
        print("Welcome to SBI ATM")
    else:
        print("INVALID PIN")
else:
    print("please enter 4 digit number")

--------------------------------------------------------------
for statement
---------------
--->used to itterate over a sequence
---> after the word "for" it is called instant variable(also called
    as loop variable.
--->range() is used to generate a sequence of numbers.
    range() is in-build function use to generate number in sequence
    manner

----> else in "for" once the itterations completed this else will be
--->The else block executes when the loop finishes normally
    (without break)
any="python"
for k in any:
    print(k)

break
---------
--->used to exit the loop based on the condition
---------
continue
---------
--->used to skip the current itterations based on the condition
---------
pass
---------
--->Python does not allow empty blocks, so pass is used as a
    placeholder.

for i in range(1,10):
    print(i)
    if i==5:
        continue


while is ----> for + if
------------->while loop in Python is used to repeat a block
              of code as long as a condition is True.






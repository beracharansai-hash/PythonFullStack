'''
condition statements
----------------------

if----------> to check the statement is true or not
if-else----->else in the if statement,incase the condition becomes
             false then it will enter into fall-back(else),it will
             execute whatever inside it
nested if
elif


num=11
if num%2==0:
    print(f"{num} is a even number{num}")
else:
    print(f"{num} is a odd number")


age_=int(input("enter the age :"))
if age_>=18:
    print("you are eligible to vote")
else:
    print(f"you have to wait for {18-age_}years")



num=8
num_2=5
if num>num_2:
    print(f"{num} is greater than {num_2}")
else:
    print(f"{num_2} is greater than{num}")



year_=2024
if (year_%4==0 and year_%100!=0) or (year_%400==0):
    print(f"{year_} is a leap year")
else:
    print(f"{year_} is not a leap year")


vowel_=input()
if vowel_ in "AEIOUaeiou":
    print(f"{vowel_} is a vowel")
else:
    print(f"{vowel_} is a consonent")
    

marks=int(input("Enter your marks"))
if marks >=45:
    stu_name=input("Enter the name")
    print(f"{stu_name} your are passed")
else:
    print(f"{stu_name}you are failed")


num=75
if num%3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print("not divisible")

'''
























    

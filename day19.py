'''
error handlimg
---------------
try block ---> the try block ,test a block of code for error

except block
---------------
the except block let hand if the code contain error


else block
---------------
This will be executed ,if the try block has no error in the code


Finally block
---------------
This will be executed either try block contain error or not



try:
    print(10/0)

except:
    print('this will handle zerodivisionerror')


try:
    print("hai")
except:
    print('this will handle zerodivisionerror')

else:
    print("No error")


try:
    print(a)
    print(5+"py")

except TypeError:
    print("this will handel name error")
except NameError:
    print("This will handle name error")

else:
    print("no error")




try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input.")
finally:
    print("Program ended.")

'''

try:
    num=int(input("Enter a number"))
    print(100/num)

except ValueError:
    print("It is tvalue error")

else:
    print("no error")

finally:
    print("program ended")
    


























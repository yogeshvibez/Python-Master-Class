# This Is My 7th Python07.py File 
# Building a Basic Calculator
import time
from math import *

num_1 = int(input("Enter Your 1st Number : "))
num_2 = int(input("Enter Your 2th Number : "))
choice = input("What Your want type +,*,%,- : ")
error = "Error Bro You have Only these options +,*,%,- try again"

if(choice == '+'):
    print("Your Sum : ",num_1 + num_2)

elif(choice == '*'):
    print("Multiples : ",num_1 * num_2)

elif(choice == '%'):
    print("Your Remainder : ",num_1 % num_2)


elif(choice == '-'):
    print(": ",num_1 - num_2)

else:
    print(error.title)
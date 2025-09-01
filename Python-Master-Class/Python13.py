# This Is My 13th Python13.py File
# If Statements & Comparisons
import subprocess
import os
import time
info = "If Statements & Comparisons"
time.sleep(0.1)
print(info.title())


def number(num1,num2,num3):
    if(num1 >= num2 and num1 >= num3):
        h = f"Your 1st Number is bigger : {num1}"
        return h
    elif(num2 >= num1 and num2 >= num3):
        d = f"Your 2th Number is Bigger : {num2}"
        return d
    else:
        k = f"Your 3th Number is Bigger : {num3}"
        return k
    
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2th Number : "))
c = int(input("Enter 3rd Number : "))

result = number(a,b,c)

print(result)
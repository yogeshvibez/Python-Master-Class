# Write a function safe_divide(a, b) that returns the result of a / b.
# If b == 0, return "Cannot divide by zero".
# Test it with safe_divide(10, 2) and safe_divide(5, 0).
import time
import subprocess


def safe_divide(a, b):
    if(b == 0):
        print("Cannot Divide By Zero")
    elif(a == 0):
        print("Cannot Divide By Zero")
    else:
        time.sleep(0.5)
        print("\n\nYour Value is ",a/b,"\n\n")


try:
    c = int(input("Enter Your 1st Number : "))
    d = int(input("Enter Your 2th Number : "))
except ValueError:
    print("INVAILD VALUE : TRY AGAIN!")

subprocess.run("cls",shell=True)
safe_divide(c,d)
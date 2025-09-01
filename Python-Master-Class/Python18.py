# This Is My 18th Python18.py File
# Exponent Function
import time
import random
import os
import subprocess
from math import *
info = ("Exponent Function in Python18.py File")
time.sleep(0.2)
print("\n\n",info.title(),"\n\n")


def raise_to_power(num1,num2):
    c =  num1**num2
    return c

ask_num1 = int((input("Enter Your Number One : ")))
ask_num2 = int((input("Enter Your Number You Want to Raise to Power : ")))

con = raise_to_power(ask_num1,ask_num2)
print(f"Your Value is : {con} ")
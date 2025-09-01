# Reverse a string entered by the user. (Hint: "hello"[::-1] → "olleh")
import time
import subprocess
import os
os.system("cls")
word = str(input("Enter Your WORD To Reverse : "))
time.sleep(0.2)

print("\n\n",word[::-1],"\n\n")
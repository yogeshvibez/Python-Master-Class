# Write a program to check if a number is even or odd
import time


try:
    num = int(input("Enter Your Number To Check Its Even : "))
except:
    print("Invalid Input : Try Again")

m = num%2

time.sleep(0.2)
if(m == 0):
    print(f"Your Number {num} Is Even")

else:
    print(f"Your Number {num} Is Not Even")
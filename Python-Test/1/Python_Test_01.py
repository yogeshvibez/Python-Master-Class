# Print your name and age in one line.
import time
time.sleep(0.06)
try:
    name = str(input("Enter Your Name : "))
    fav = int(input("Enter Your fav number : "))
except:
    print("Invalid Input: Try Again")


print(f"Hello {name} Your Fav Number is : {fav}")
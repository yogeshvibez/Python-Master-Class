# Write a program to check if someone is eligible to vote (age >= 18).
import time

try:
    age = int(input("Enter Your Age : "))
except:
    print("Your Value Is Invalid : Try Again")

time.sleep(0.4)
if(age >= 18):
    print("\nYou can Vote\n")
elif(age == 17):
    print("\nWaite One Year To Vote\n")
else:
    print("\nYou Cant Vote Rigth Now Until 18\n")
# This Is My 16th Python16.py File
# Building a Guessing Game
import os
import subprocess
from math import *
import time
import random
info = "Building a Guessing Game In Python16.py"
time.sleep(0.1)
print("\n\n",info.title(),"\n\n")

guess_name = "Yogesh"
guess = ""
guess_limit = 6
guess_count = 0
out_of_guess = False

while(guess_name != guess and not(out_of_guess)):
    if(guess_count < guess_limit):
        guess = input("Enter Your Guess : ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess == True:
    print("You Lose")

else:
    print("You win")
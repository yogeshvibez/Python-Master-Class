import random

# Generate a random integer between 1 and 100 (inclusive)
random_number = random.randint(1, 100)

guess = 90, 90
guess_count = 0
count_limit = 1, 1
limit = 3

try:
    for i in guess and not count_limit:

        c = int(input("Enter Number Guess : "))
        if(c == 90):
            f"YOU WON THE GAME Real Value: {i}"

        elif(c <= 77 or c >= 101):
            print("Too High")
        elif(c >= 78 or c <= 99):
            print("Close")
        else:
            "Wrong Input"
        guess_count = guess_count + 1
        
        if(guess_count < limit):  
            count_limit = 1,1
        else:
            count_limit = True    
except:
    print("Limit ADD ON")

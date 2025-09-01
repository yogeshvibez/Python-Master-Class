# This is my 4th Python04.py file
# Variables & Data Types
import time
time.sleep(0.2)
print("\n","Variables & Data Types : ")
time.sleep(0.5)

Funny = """⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀              ⢀⣀⣀⣠⣤⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⢀⣀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢋⣭⡍⣿⣿⣿⣿⣿⣿⠀
⠀⢀⣴⣶⣶⣝⢷⡝⢿⣿⣿⣿⠿⠛⠉⠀⠀⣰⣿⣿⢣⣿⣿⣿⣿⣿⣿⡇
⢀⣾⣿⣿⣿⣿⣧⠻⡌⠿⠋⠁⠀⠀⠀⠀⢰⣿⣿⡏⣸⣿⣿⣿⣿⣿⣿⣿
⣼⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⠇⢻⣿⣿⣿⣿⣿⣿⡟
⠙⢹⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⡿⠟⠁"""



ask_job = str(input("Sir Which Type Of Job Are You Like : "))
time.sleep(0.7)
print("\n\n",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".")
print("Sir Elon Musk Hire You At This Job : \n",Funny,"\n\n")

ask_gender = input("Hello Type Your Gender Male For ':M:' Women For ':W:'  : ")

if(ask_gender.capitalize == 'm'):
    print("\nWelcome Malehub ElonMusk Assign You ",ask_job)

elif(ask_gender == 'M'):
    print("\nWelcome Malehub ElonMusk Assign You ",ask_job)

elif(ask_gender == 'w'):
    print("\nI think You Bich Take This Job : \n\n",Funny)

elif(ask_gender == 'W'):
    print("\nI think You Bich Take This Job : \n\n",Funny)

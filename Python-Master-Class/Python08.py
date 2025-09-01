# This Is My 8th Python08.py File
# List
import time
from math import *
import subprocess
import os

time.sleep(0.2)
print("List\n\n")
time.sleep(0.2)

# Name = str(input("Enter Your Name : "))
# Age = int(input("Enter Your Age : "))
# Location = str(input("Enter Your City Name : "))
subprocess.run('cls', shell=True)
os.system("notepad.exe")
i = 5
# for i in range(10):
#     print('You Got Fucked')
#     subprocess.Popen("notepad.exe")


# list_ = [f"\n\n\n\nName = {Name}",f"Age = {Age}",f"Location = {Location}"]
time.sleep(0.2)
# print(list_[0],"\n",list_[1],"\n",list_[2])
print("\n\n")

_list2 = [1,2,3,4,5,6,7,8,9,10]
_list = ["Mohlu","Monu","Noni","khusu","gatik","pawan"]
p = _list[5] = "pawan gand maro"
print(_list)
print(_list[1:5])
_list2.extend(_list)
_list2.append("Tum-Sub-Ki-MAA-Ka-Bhosda")
_list2.insert(2,"land")
_list2.remove("land")
t = _list2.index("Mohlu")
print(_list2,'\n',f"index is {t}")

copy_list = _list2.copy()
print(copy_list)
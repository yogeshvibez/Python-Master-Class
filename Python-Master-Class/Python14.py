# This Is My 14th Python14.py File
# Dictionaries
import time
import os
import subprocess
time.sleep(0.06)
info = "\n\nDictionaries in Python14.py File\n\n"
print(info.title())
time.sleep(0.06)


user = {
    "name": "Yogesh",
    "Age": 16,
    "Location": "Gurugram"
}

print("\n\n",user," = ",type(user) )
print("\n\n",user["name"])
print("\n\n",user.get("Location"))


user_friend = {
    "name": ["Mohlu","Monu","Noni","Khusu","Pawan","Gatik"],
    "Age": [16,15,14,17,19,16],
    "location": ["gurugram","ch","ch","ch","ch","ch"]
}

for name, locatio in user_friend.items():
    print("\n\n",f"Name : {name}","     ",f"Location : {locatio}")
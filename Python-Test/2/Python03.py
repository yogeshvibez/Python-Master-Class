# Create a dictionary of 3 students with their marks (e.g., {"Alice": 85, "Bob": 70, "Yogesh": 90}).
# Print the student with the highest marks.
import time
import subprocess

dicti = {"Alice": 85, "Bob": 70, "Yogesh": 90}
if(dicti["Alice"] > dicti["Bob"] and dicti["Alice"] > dicti["Yogesh"]):
    print("\n\nAlice : ",dicti["Alice"])
elif(dicti["Yogesh"] > dicti["Alice"] and dicti["Yogesh"] > dicti["Bob"]):
    print("\n\nYogesh : ",dicti["Yogesh"])
else:
    print("\n\nBob : ",dicti["Bob"])
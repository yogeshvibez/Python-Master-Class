# Print all numbers from 1 to 20 using a loop.
import time
import subprocess

try:
    num = int(input("Enter A Number Where You want Print : "))
except:
    print("INVAILD INPUT : ENTER INTEGER")

subprocess.run("cls",shell=True)

for i in range(1,num):
    time.sleep(0.09)
    print(i)
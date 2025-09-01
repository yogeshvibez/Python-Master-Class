# Print the multiplication table of a number given by the user (example: 5 → 5x1=5 … 5x10=50).
import time
import subprocess

table_num = int(input("Enter Your Number You want to PRINT Table of That num : "))
c = 1
subprocess.run("cls", shell=True)
while(c <= 10):
    time.sleep(0.1)
    print(f"{table_num}X{c} = ",table_num*c)
    c = c +1
# This Is My 19th Python19.py File
# Try\Except
import time
info = '"Try and Except In Python19.py File"'
time.sleep(0.2)
print("\n\n",info.title(),"\n\n")
try:
   
   Age = int(input("Enter Your Age: "))
   print(f"Your Age {Age}")
except:
   print("INVALID INPUT")
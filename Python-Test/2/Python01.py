# Level 1 – File Handling
# Write a program that asks the user for a sentence and saves it into a file notes.txt.
# Then, read back the file and print the contents.
# Add a feature that clears the file before writing new text.
import time
import subprocess

try:
    text = input("Enter Your Any sentence to Save in Notes.txt : ")
    subprocess.run("cls",shell=True)
except ValueError:
    print("You Enter Invaild Text For Code")
subprocess.run("cls", shell=True)
time.sleep(0.1)
print("\n\n")
time.sleep(0.05)
Notes = open(r"Python-Test\2\Notes.txt", "w")
time.sleep(0.009)
write = Notes.write(f"'{text}'")
time.sleep(0.1)
print(f"       Your Text Updated \n\n{text}\n")
Notes.close()
time.sleep(0.3)
print("\nYour File Closed Safe and Secure 100%\n\n")


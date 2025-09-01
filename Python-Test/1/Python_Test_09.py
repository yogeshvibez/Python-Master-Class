# Write a function greet(name) that prints "Good morning, <name>".
import time
import subprocess


def greet(name):
    print(f"Good Morning {name}")

a = str(input("Enter Your Name : "))

greet(a.title())
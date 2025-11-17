"""
Name: Areeb Khan
Enrollment: 0103CS231080
Batch: 6
Batch Time: 12:10 to 13:50
Assignment: 3
"""
# Importing Modules
import time, os

def clear():
    os.system("clear")

def write(string):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(0.015)
    print()
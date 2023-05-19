#!/usr/bin/env python3

# Prompt the user to enter a score
score = input("Enter Score: ")

try:
    # Convert the input to a floating-point number
    scr = float(score)
except:
    # Handle the exception if the input cannot be converted to a float
    print("Value is out of range")
    quit()

# Determine the grade based on the score
if scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
else:
    print("F")


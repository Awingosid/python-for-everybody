#!/usr/bin/env python3

# Prompt user for hours and rate per hour
hrs = input("Enter hour(s): ")
rt = input("Enter rate: ")

# convert hrs and rt to float values and  to handle potential conversion errors
try:
    hrs = float(hrs)  
    rt = float(rt)  
except ValueError:
    print("Invalid input. Hours and rate must be numerical.")
    quit()

if hrs <= 40:
    pay = hrs * rt  # Calculate pay for regular hours (up to 40)
else:
    xhrs = hrs - 40  # Calculate the number of overtime hours
    regular_pay = 40 * rt  
    overtime_pay = xhrs * (rt * 1.5)  
    pay = regular_pay + overtime_pay  # Calculate total pay (regular + overtime)

print("Your pay:", round(pay, 2))  


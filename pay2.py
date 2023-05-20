#!/usr/bin/env python3


def computepay(hrs, rt):
    # Calculate the pay based on the number of hours worked and the hourly rate
    if hrs > 40:
        # If the hours worked exceed 40, calculate regular pay for 40 hours and overtime pay for the remaining hours
        pay = (40 * rt) + ((hrs - 40) * (rt * 1.5))
    else:
        # If the hours worked are 40 or less, calculate regular pay only
        pay = (hrs * rt)
    return pay

try:
    # Prompt the user to enter the number of hours and the hourly rate
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except ValueError:
    # Handle the exception if the user enters non-numeric values
    print("Error, input numerical values!")
    quit()

# Call the computepay 
pay = computepay(hours, rate)

print("Pay:", pay)


"""
Program Name: Lab8_komalpreetkaur-1.py
Author: Komalpreet Kaur
Purpose: Check if a 12-digit UPC code is valid.
Starter Code: None
Date: 06/18/2026
"""
# This function calculates UPC check digit using standard formula
def find_UPC(first11):
    # Apply UPC check digit formula (odd + even calculation)
    # Add digits in odd positions
    odd_total = 0
    for i in range(0, 11, 2):
        odd_total += int(first11[i])

    # Add digits in even positions
    even_total = 0
    for i in range(1, 11, 2):
        even_total += int(first11[i])

    # Follow the UPC formula
    total = (odd_total * 3) + even_total

    # Find the check digit
    check_digit = (10 - (total % 10)) % 10

    return check_digit


# Ask for a UPC until the user enters a valid one
while True:
    upc = input("Enter a 12-digit UPC: ")

    if len(upc) == 12 and upc.isdigit():
        break
    else:
        print("Error: UPC must be exactly 12 numbers.\n")

# Separate the first 11 digits and the check digit
first11 = upc[:11]
user_check_digit = int(upc[11])

print()
print(f"The first 11 digits are '{first11}'.")
print(f"The provided check digit is '{user_check_digit}'.")

print("\nCalculating...")

# Calculate the correct check digit
correct_check_digit = find_UPC(first11)

print(f"The expected check digit is {correct_check_digit}.")
print()

# Compare the digits
if correct_check_digit == user_check_digit:
    print("This is a VALID UPC.")
else:
    print("This is an INVALID UPC.")
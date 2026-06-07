# This is a Try It Out - Coding Challenge
# Create a function that will determine whether a number is positive or negative.

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

value = int(input("Enter a number: "))
print("Your number is:", check_number(value))
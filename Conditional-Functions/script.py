# This is a Try It Out - Coding Challenge
import operator
# Write a program that generates a random number between 1 and 100.
# The user has to guess the number in a limited number of attempts.
# Provide feedback after each guess (higher, lower, or correct).

import random

number1 = int(input("Guess the number: "))
number2 = random.randint(1, 100)

if number1 == number2:
    print('You guessed right', '\n')
else:
    if number1 > number2:
        print('Number is higher than the number', '\n')
    elif number1 < number2:
        print('Number is lower than the number', '\n')
    else:
        pass

# Write a program that allows the user to enter two numbers and an operator (+, -, *, /)
# perform the corresponding calculation.

# Function to perform calculations
def calculate():
    try:
        # Prompt user
        num1 = int(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = int(input("Enter second number: "))

        # Use conditional statements to determine which operation to perform
        if operator == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif operator == '/':
            # Check for division by zero to prevent a crash
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            # Handle cases where the user enters an invalid operator
            print("Error: Invalid operator. Please use +, -, *, or /.")

    except ValueError:
        # Handle cases where the user enters text instead of numbers
        print("Error: Invalid input. Please enter numerical values.")
    except ZeroDivisionError:
        # Handle cases where the user enters zero
        print("Error: Division by zero is not allowed.")

# Run the calculator
calculate()

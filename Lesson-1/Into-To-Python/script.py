# This is a Try It Out - Coding Challenge

# Create a program that acts as a simple calculator.
# It should take two numbers and an operator (+, -, *, /) as input and perform the corresponding arithmetic operation.
# Add comments to explain each part of the code.

def simple_calculator(num1, num2):
    return num1 + num2

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print('The addition result is', simple_calculator(num1, num2),'\n')

#Write a program that generates and prints a random number between 1 and 100.
# Use the random library.
import random
def random_number():
    return random.randint(1, 100)

print("Your random number is:", random_number(),'\n')

# Write a program that calculates and prints the square root of a given number using the math.sqrt() function.
import math
def square_root(num):
    return math.sqrt(num)

num = int(input('Enter a number: '))
print('The square root is', square_root(num))
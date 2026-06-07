# Try Except
# The Problem: Think about the int() function. It works fine if the user types "20", but if they type "twenty", the program crashes with a ValueError.
# In a real app, you don't want the whole program to shut down; you want to tell the user, "Hey, please enter a number!"

try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except:
    print("Error: Please enter a valid whole number.")

print("The program is still running!", '\n')

'''
Common Exception Types:
ValueError: When a function gets an argument of the right type but inappropriate value (like int("hello")).
ZeroDivisionError: When you try to divide a number by zero.
TypeError: When an operation is applied to an object of the wrong type.
'''

try:
    number = int(input("Enter a number to divide 100 by: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid Input: You must enter a number.")
except ZeroDivisionError:
    print("Math Error: You cannot divide by zero.")
# This is a Try It Out - Coding Challenge

# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

def temperature(num):
    return num * (9 / 5) + 32

num = int(input("Enter Celsius temperature: "))
print(num, "degrees is equals to ",temperature(num), "fahrenheit")
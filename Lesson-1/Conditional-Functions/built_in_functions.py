# Intro & Built In Functions
# Function is a named, reusable sequence of statements that performs a specific computation.

result = int(input("Enter a value: ")) #int is a built-in function
print(type(result), '\n') # type is also a built-in function

# Why Use Functions? functions are the building blocks of clean code.

# Write a script that calculates travel time while accounting for random weather conditions.
"""
    Clear Skies: Normal speed (1.0x multiplier).
    Heavy Rain: 50% slower (1.5x multiplier).
    Snow Storm: 200% slower (3.0x multiplier).
"""
import random
import math

print("--- Smart Route Estimator ---")

# 1. THE JOURNEY: Generate a random distance between 5 and 50 miles
distance = random.randint(5, 50)
speed = 60 # We assume a base speed of 60 miles per hour (1 mile per minute)

# 2. THE CONDITION: Pick a random weather condition from a list
weather = random.choice(["Clear", "Rainy", "Snowy"])

# 3. THE MULTIPLIER: Use conditionals to set the delay based on weather
if weather == "Snowy":
    multiplier = 3.0
elif weather == "Rainy":
    multiplier = 1.5
else:
    multiplier = 1.0

# 4. THE CALCULATION:
# Time = (Distance / Speed) * 60 minutes * multiplier
raw_time = (distance / speed) * 60 * multiplier

# 5. THE POLISH: Use math.ceil
# We round UP because it is better to tell a user they will arrive in
# 15 minutes and have them arrive early, rather than telling them 14
# and having them arrive late.
final_time = math.ceil(raw_time)

# 6. THE OUTPUT: Display the results to the user
print("Distance to destination: " + str(distance) + " miles")
print("Current Weather: " + weather)
print("Estimated Travel Time: " + str(final_time) + " minutes")
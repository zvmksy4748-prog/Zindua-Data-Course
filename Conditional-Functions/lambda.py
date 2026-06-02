# Lambda Functions - Anonymous Functions
# Normally, when we want to create a function, we use the def keyword.
# However, sometimes we need a quick, one-time-use function that is so simple we don't even want to give it a name.

'''
The Key Characteristics:
Anonymous: They have no name (unless you assign them to a variable).
Single-Line: They can only contain one single expression.
Auto-Return: You don't type the word return. They automatically return the result of the expression.
'''

# A function that adds 10 to any number
add_ten = lambda x : x + 10

print(add_ten(5))  # Output: 15

# A function to calculate the area of a rectangle
calculate_area = lambda length, width : length * width

print(calculate_area(10, 5)) # Output: 50

# A function to check if a player is strong enough to enter a dungeon
check_strength = lambda power : "Enter" if power > 50 else "Too Weak"

print(check_strength(65)) # Output: Enter
print(check_strength(30)) # Output: Too Weak

# Why Use Lambda Functions
# Lambdas are most powerful when used inside other functions.
# This allows you to create "Function Factories"â€”functions that help you build other functions.

calculate_tax = lambda price: price * 1.15
is_expensive = lambda price : "True" if price > 50  else "False"
print(is_expensive(10))
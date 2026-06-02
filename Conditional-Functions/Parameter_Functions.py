# Parameters: The variables listed in the function's definition (the "slots" waiting to be filled).
# Arguments: The actual values you pass into those slots when you call the function.

# 'bruce' is a parameter (the placeholder)
def print_twice(bruce):
    print(bruce)
    print(bruce)

# 'Spam' is the argument (the actual value)
print_twice('Spam')

# Types of Parameters
# Positional Parameters - The order in which you provide the arguments matters
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet('hamster', 'Harry') # Correct
describe_pet('Harry', 'hamster') # Error in logic: "I have a Harry named hamster."

# Keyword Arguments - You can skip the "order" rule by explicitly naming the parameter during the call.
# This makes it clear what each value represents.
describe_pet(pet_name='Bronnie', animal_type='Dog') # Order doesn't matter here

# Default Parameters - You can provide a fallback value for a parameter.
# If the caller doesn't provide an argument for it, Python uses the default.
def greet(name, message="Hello"):
    print(f"{message}, {name}!", '\n')

greet("Alice")           # Output: Hello, Alice!
greet("Bob", "Good day") # Output: Good day, Bob!

# Variable-Length Parameters - sometimes you don't know how many items will be passed.
# *args collects extra positional arguments into a tuple.
# **kwargs collects extra keyword arguments into a dictionary.
def make_pizza(size, *toppings):
    print(f"Making a {size} pizza with: {toppings}")

make_pizza('large', 'pepperoni', 'mushrooms', 'extra cheese')
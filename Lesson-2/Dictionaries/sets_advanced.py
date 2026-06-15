# Sets Advanced Concepts

# The "Unique List" Idiom
# The most common practical application of sets in general scripting is removing duplicates from a list.
raw_data = ["apple", "banana", "apple", "orange"]

# Convert to set to remove duplicates, then back to list
clean_data = list(set(raw_data))

print(clean_data)
# Output: ['banana', 'apple', 'orange']

# Aliasing vs. Copying
# Because sets are mutable objects, using the assignment operator = only creates a reference (alias), not a copy.
# 1. Aliasing (Dangerous)
A = {1, 2}
B = A         # B points to the same memory as A
B.add(3)
print(A)      # {1, 2, 3} (A is modified!)

# 2. Copying (Safe)
A = {1, 2}
B = A.copy()  # B is a new independent set
B.add(3)
print(A)      # {1, 2} (A is safe)

# Frozen Set
# immutable version of a set. Once created, it cannot be changed.
# Creating a frozenset
fs = frozenset([1, 2, 3])
# fs.add(4) # Raises AttributeError

# Valid nesting
nested_set = {frozenset({1, 2}), frozenset({3, 4})}


# Set Comprehensions
# Example: Create a set of even numbers squared
numbers = [1, 2, 3, 4, 5, 5] # Duplicate 5
squares = {x**2 for x in numbers if x % 2 == 0}

print(squares)
# Output: {16, 4} (2 squared is 4, 4 squared is 16. Duplicates handled auto)
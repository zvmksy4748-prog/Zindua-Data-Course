# Sets Foundations
# It is modeled after the mathematical definition of a set in algebra.

'''
There are two primary ways to create a set: using curly braces {} or the set() constructor.
A common mistake is assuming {} creates an empty set. In Python, {} creates an empty Dictionary.
    To create an empty set, you must use the constructor.
While the set itself is mutable (you can add/remove items),
    the elements contained within the set must be immutable (specifically, they must be "hashable").
'''

# Set of integers
ids = {101, 102, 103}

# Set of mixed immutable types
mixed = {1, "Hello", 3.14, (1, 2)}

# INCORRECT way to create an empty set
my_set = {}
print(type(my_set)) # <class 'dict'>

# CORRECT way to create an empty set
my_set = set()
print(type(my_set)) # <class 'set'>

# Modifying Sets
s = {1, 2}
s.add(3)            # s is {1, 2, 3}
s.update([3, 4, 5]) # s is {1, 2, 3, 4, 5} (3 is ignored as duplicate)

'''
remove(val): Removes the item. Raises KeyError if the item is missing.
discard(val): Removes the item. Does nothing if the item is missing (fails silently/safely).
pop(): Removes and returns an arbitrary (random) item. Used when you want to process items until the set is empty. Raises KeyError if the set is empty.
clear(): Removes all items, leaving an empty set.
'''
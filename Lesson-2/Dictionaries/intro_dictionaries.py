# Dictionaries Overview
# It allows you to store data as Key-Value pairs. {}
from urllib import request

'''
In a List,
    you access elements using an index, which must be an integer (0, 1, 2...).
    The order is strictly defined by position.
In a Dictionary,
    the indices can be (almost) any type. We call these indices Keys. Each key maps to a specific Value.
'''

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(counts.get('jan', 0))

# Looping Through Dictionaries
for key in counts:
    print(key, counts[key]) # Must use counts[key] to get the value


# Sorting Dictionaries
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

# Step 1 & 2: Get keys and sort them
lst = list(counts.keys())
lst.sort()
print("Sorted keys:", lst) # Output: ['annie', 'chuck', 'jan']

# Step 3: Iterate the sorted list
for key in lst:
    print(key, counts[key])
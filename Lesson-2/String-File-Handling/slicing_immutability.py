# Slicing Immutability
# Slicing allows you to "cut" a specific substring out of a larger string without modifying the original.

'''
The Standard Syntax: [start:stop]

Start Index: The position where the slice begins (Included).
Stop Index: The position where the slice ends (Excluded).
'''

# Understanding the "Up to but not including" rule
message = "Python Programming"

# Extract 'Python'
# P y t h o n
# 0 1 2 3 4 5
# To get 'Python', we must stop at index 6 (the space).
# 6 - 0 = 6. The result has 6 characters.
print(message[0:6]) # Output: 'Python'

# Slicing Shortcuts (Omissions)
fruit = "strawberry"
print(fruit[:5])  # 'straw'
print(fruit[5:])  # 'berry'
print(fruit[:])   # 'strawberry'

# The "Update" Pattern (Reconstruction)
base_filename = "report.txt"
# Let's change the extension to .pdf
new_filename = base_filename[:-3] + "pdf"
print(new_filename) # 'report.pdf'

# The "Step" Parameter
# The step value determines the "stride" or how many characters to skip.
numbers = "0123456789"

# Every second character (Evens)
print(numbers[0:10:2]) # '02468'

# The "Instant Reverse" Trick
# By using a step of -1, Python crawls backward through the string.
print(numbers[::-1]) # '9876543210'
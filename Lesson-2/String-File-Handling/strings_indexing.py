# Strings Intro Indexing

# Python does not care whether you use single quotes or double quotes—both create identical string objects.
# Each character has a position called an index. Python uses zero-based indexing, which means counting starts at 0, not 1.

fruit = 'banana'

print(fruit[0]) # Output: 'b'

# String Length - returns the total number of characters in a string.
#  The last valid index of any string is always Length - 1.

last_index = len(fruit) - 1
print(fruit[last_index]) # Output: 'a'

# Negative Indexing - Calculating len(string) - 1 every time you want the end of a string is tedious.
# Negative indexing counts backward from the end of the string, starting with -1.

print(fruit[-1]) # Output: 'a'
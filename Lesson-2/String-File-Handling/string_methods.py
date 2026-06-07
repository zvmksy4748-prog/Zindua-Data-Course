# String Methods

# In Python, a string is not just a piece of data; it is an Object.
# Objects come with built-in functions called Methods that are specifically designed to manipulate that object.

word = "python"
word.upper()
print(word) # Still "python" - the original was not touched!

word = word.upper() # This captures the new string created by the method
print(word) # Now "PYTHON"

# Case Modification Methods
'''
.upper()        Converts all characters to uppercase.       "hi".upper() -> "HI"
.lower()        Converts all characters to lowercase.       "HI".lower() -> "hi"
.capitalize()   Capitalizes only the very first letter.     "hello world".capitalize() -> "Hello world"
.title()        Capitalizes the first letter of every word. "jane doe".title() -> "Jane Doe"
.swapcase()     Flips upper to lower and vice versa.        "pYTHON".swapcase() -> "Python"
'''

# Searching and Counting Methods
'''
.find(substring)    Searches for a substring and returns the index of the first occurrence.
.count(substring)   Counts how many times a substring appears in the string.
'''

# Cleaning Methods
'''
.strip()        Removes whitespace from both the left and right ends.
.lstrip()       Removes whitespace from the left side only.
.rstrip()       Removes whitespace from the right side only.
'''

# Validation Methods (The Boolean Checkers)
'''
.startswith(prefix):    Does it start with this text?
.endswith(suffix):      Does it end with this text?
.isdigit():             Is the string composed only of numbers? (Great for checking input before using int()).
.isalpha():             Is the string composed only of letters?
'''

# Transformation methods
# .replace(old, new)
text = "I like apples. Apples are the best."
# Note: replace is case-sensitive!
new_text = text.replace("apples", "oranges")
print(new_text) # "I like oranges. Apples are the best."

# .split(delimiter) - Breaks a string into a List of smaller strings based on a "delimiter" (separator).
sentence = "Python is a powerful language"
words = sentence.split()
print(words) # ['Python', 'is', 'a', 'powerful', 'language']

data = "apple,orange,banana,grape"
fruit_list = data.split(",") # Split at every comma
print(fruit_list) # ['apple', 'orange', 'banana', 'grape']

# .join(iterable) - The inverse of split.
# It takes a list of strings and glues them together using a specific string as the glue
fruits = ['apple', 'orange', 'banana']
glue = " | "
result = glue.join(fruits)
print(result) # "apple | orange | banana"

# Pro Tip: Use an empty string to join characters
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars)) # "Python"


# Method Cleaning
# The Goal: Clean up messy email data
raw_email = "   USER_Name@UCT.AC.ZA   \n"

# 1. strip() -> "USER_Name@UCT.AC.ZA"
# 2. lower() -> "user_name@uct.ac.za"
# 3. replace() -> "user.name@uct.ac.za"
clean_email = raw_email.strip().lower().replace("_", ".")

print(clean_email) # "user.name@uct.ac.za"
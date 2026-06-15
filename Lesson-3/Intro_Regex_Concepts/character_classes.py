# Character Classes

# The Wildcard: Dot (.)
'''
The dot is the most powerful and dangerous character in Regex. It is often called the "Wildcard."
    Definition: Matches ANY single character.
    What it includes: Letters, numbers, symbols (@, #, &), and spaces.
    The Only Exception: It does not match a newline (\n).
'''

import re

# Scenario: We are scraping a document for variations of a word.
# We know it starts with 'Gr' and ends with 'y', but the middle letter varies.
text = "The sky was Gray, the shirt was Grey, the alien was Graay."

# Pattern Logic:
# 1. Match 'Gr'
# 2. Match ONE character of any kind (.)
# 3. Match 'y'
matches = re.findall(r"Gr.y", text)

print(matches) # Output: ['Gray', 'Grey']

# The "Literal Dot" Trap

# Since . means "Any Character", how do we find an actual period at the end of a sentence?
# The Solution: Escape it with a backslash \.
# r"www.google.com" matches "www@googleZcom" (Because dots are wildcards).
# r"www\.google\.com" matches "www.google.com" (Because we escaped them).

# Digits - Digits (\d) and Non-Digits (\D)
'''
Data science often involves extracting IDs, phone numbers, or prices.
    Symbol:  (lowercase d). Matches any single digit (0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
    The Opposite: (uppercase D). Matches anything that is NOT a digit.
'''

text2 = "Project A: file_25, Project B: file_9"
match2 = re.findall(r"file_\d\d", text2)

print(match2) # Output: ['file_25']
# WHY 'file_9' FAILED: The pattern demanded TWO digits (\d\d).

# Word Characters - Word Characters (\w) and Non-Words (\W)
'''
This is the standard tool for matching "names" of things: usernames, variable names, email prefixes.
    Symbol:(lowercase w) Matches "Word Characters." This includes: Letters: a-z, A-Z: Numbers: 0-9: Underscore: _
    The Opposite: (uppercase D). Matches anything that is NOT a digit.
'''
text3 = "User: python_guru! (Status: Active)"

# Pattern Logic:
# 1. Match 'User: ' literally.
# 2. Match one or more (+) word characters.
# (We will cover '+' in depth in Module 3, but it means "keep going")
match = re.search(r"User: \w+", text3)

if match:
    print(f"Found: '{match.group()}'") # Output: Found: 'User: python_guru'
    # It STOPPED at '!' because '!' is NOT a \w character.
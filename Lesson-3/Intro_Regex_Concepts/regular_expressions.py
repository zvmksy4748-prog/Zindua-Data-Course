# Regex Foundations

# The Regex Approach: Concept: You are not searching for a specific string; you are searching for a rule or a blueprint.
# "Find a word that starts with 'C', has an 'l' and 'r' in the middle, and ends with a vowel or consonant, regardless of case."

import re
'''
The Raw String (r)
    By adding a lowercase r before the opening quote (r"..."), you tell Python:
    "Turn off your internal escape characters. Treat every backslash inside these quotes as a literal character.
    Do not process them."
    Always use it even if you don't need it.
'''

# The Basic Search: re.search()
# It checks until it finds a match or runs out of text.
# If the end of the string is reached with no match, it returns None.

text = "Order ID: 59392"

# Detailed Breakdown of Execution:
# 1. Pattern: r"Order"
# 2. Engine checks index 0 ('O') -> Match!
# 3. Stops scanning. Returns Match Object.
match = re.search(r"Order", text)

# We check if 'match' is truthy (exists)
if match:
    print("Pattern found!")
    print("Match Object:", match) # Output: <re.Match object; span=(0, 5), match='Order'>
else:
    print("Pattern not found.")

# Critical Distinction: re.search() vs re.match()
# re.match(): Checks ONLY the very beginning of the string. If the pattern is at character 2, it fails.
# re.search(): Checks ANYWHERE in the string.


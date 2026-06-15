# Extraction Groupings Quantifiers
# Move from simply asking "Does this pattern exist?" to saying "Find this pattern and extract specific pieces of data from it."

import re

text = "Errors: 404, 500. Phone: 123-4567. Color: colour."

# 1. Plus (+): Find sequences of digits
# Matches "404", "500", "123", "4567"
print(re.findall(r"\d+", text))

# 2. Curly Braces {}: Find phone segments
# Look for exactly 3 digits, hyphen, exactly 4 digits
print(re.findall(r"\d{3}-\d{4}", text)) # ['123-4567']

# 3. Question Mark (?): Handle British/American spelling
# Matches 'u' zero times or one time.
print(re.findall(r"colou?r", text), '\n') # ['colour']

# re.findall() vs re.search()
'''
search: Purpose is Verification / Control Flow.
    When to use: "Is this user input valid?" or "Does this log line contain an error?"
findall: Purpose is Extraction / Data Mining.
    When to use: "Give me every email address in this document."
'''
text2 = "The winning numbers are 10, 20, and 30."

# SEARCH: Lazily stops at the first one.
match2 = re.search(r"\d+", text)
if match2:
    print(match2.group()) # Output: 10

# FINDALL: Greedily grabs them all.
all_matches = re.findall(r"\d+", text2)
print(all_matches, '\n') # Output: ['10', '20', '30']

# The Power of Groups ()
# This is the "Sniper" feature of Regex.
# Sometimes we need to match a long pattern to ensure we have the right context, but we only want to keep a small part of it.

log = "Time=14:00 Level=ERROR"

# APPROACH 1: No Groups (Messy)
# We match the label to ensure context, but we get the label in the output.
print(re.findall(r"Time=\d+:\d+", log)) # Output: ['Time=14:00'] -> We have to clean this string later.

# APPROACH 2: With Groups (Clean)
# We match "Time=", but we only CAPTURE (\d+:\d+)
# We match "Level=", but we only CAPTURE (ERROR)
times = re.findall(r"Time=(\d+:\d+)", log)
print(times, '\n')  # Output: ['14:00']

# Advanced: Double Extraction
email_log = "From: john@gmail.com, To: jane@yahoo.com"

# Pattern: Match "From: ", capture the name, match "@", capture the domain
# We use parens twice.
matches = re.findall(r"From: (\w+)@(\w+\.\w+)", email_log)

print(matches) # Output: [('john', 'gmail.com')]
# Now you have the user and the domain separated!

# Greedy vs. Lazy Matching
import re

html = "<b>Bold</b> <i>Italic</i>"

# GREEDY (The Default)
# Matches from the first < to the LAST >
greedy = re.findall(r"<.+>", html)
print(greedy)
# Output: ['<b>Bold</b> <i>Italic</i>'] (One giant string!)

# LAZY (The Fix)
# Matches from < to the FIRST >
lazy = re.findall(r"<.+?>", html)
print(lazy)
# Output: ['<b>', '</b>', '<i>', '</i>'] (Distinct tags)
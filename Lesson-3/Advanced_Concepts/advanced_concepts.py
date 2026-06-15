# Advanced Concepts
# Write Regex code that is maintainable (easy to read), robust (handles messy real-world data), and efficient (doesn't crash your memory).

# Syntax: (?P<name>...): Named Groups
import re

log_entry = "Event: LOGIN_SUCCESS User: admin_01 Time: 14:30"

# FRAGILE WAY (Numbered Groups)
# If we add anything to the start of this pattern, indexes shift.
fragile_pattern = r"Event: (\w+) User: (\w+) Time: (\d+:\d+)"

# PROFESSIONAL WAY (Named Groups)
# We embed the keys 'event', 'user', and 'time' into the pattern.
robust_pattern = r"Event: (?P<event>\w+) User: (?P<user>\w+) Time: (?P<time>\d+:\d+)"

match = re.search(robust_pattern, log_entry)
match2 = re.search(fragile_pattern, log_entry)

if match:
    # 1. Access by Name (Readable)
    print(f"User: {match.group('user')}")
    print(f"Action: {match.group('event')}")

    # 2. Convert to Dictionary (Powerful)
    # This creates: {'event': 'LOGIN_SUCCESS', 'user': 'admin_01', 'time': '14:30'}
    data = match.groupdict()
    print(data['time'])

if match or match2:
    print(match.group())
    print(match2.group(), '\n')

# Flags (Handling Real-World Data)
# By default, Regex is extremely strict. It is case-sensitive, and the dot . stops at newlines.
# Real-world data is rarely this clean. We use Flags to relax the rules.

'''
re.IGNORECASE (or re.I)
    Behavior: Makes the pattern match both Uppercase and Lowercase letters.
    Use Case: User input search, scraping inconsistent HTML.
re.DOTALL (or re.S)
    The Issue: By default, the wild card . matches everything except a newline (\n).
    The Fix: re.DOTALL forces the . to match newlines too.
    Use Case: Extracting a block of text that spans multiple paragraphs.
re.MULTILINE (or re.M)
    The Issue: By default, ^ matches the start of the file, and $ matches the end of the file.
    The Fix: re.MULTILINE makes ^ match the start of each line and $ the end of each line.
'''

text = """
 Start
 Title: PYTHON 
 Description: Python is a
 versatile language.
 End
 """

# Scenario: Extract everything between 'Title:' and 'End', regardless of case or newlines.
# 1. Case Insensitive (Matches 'PYTHON' even though we wrote 'python')
# 2. Dot All (Matches the newlines inside the description)
pattern = r"title: (.*?) end"

match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

if match:
    print(match.group().strip())
    print(match.group(1).strip(), '\n')

# Data Cleaning with re.sub()
# Regex isn't just for finding data; it is the industry standard tool for cleaning (Sanitizing) data.
# Logic: "Find every instance of X and replace it with Y."

text = "Item#1; Item#2; Item#3"
# Replace both '#' and ';' with a simple hyphen
clean = re.sub(r"[#;]", "-", text)
print(clean) # "Item-1- Item-2- Item-3"

date_list = "Dates: 12/31/2023 and 01/15/2024"

# Step 1: Capture the parts (Month)/(Day)/(Year)
pattern = r"(\d{2})/(\d{2})/(\d{4})"

# Step 2: Re-arrange them using \3, \1, \2
# \3 refers to the 3rd group (Year)
# \1 refers to the 1st group (Month)
# \2 refers to the 2nd group (Day)
reformatted = re.sub(pattern, r"\3-\1-\2", date_list)
print(reformatted, '\n') # Output: "Dates: 2023-12-31 and 2024-01-15"

# Efficiency: re.finditer vs re.findall
# If you run findall on a 2GB log file, Python tries to create a list containing 1 million strings. Your program will crash (Memory Error).
# finditer does not build a list. It creates a Generator.
#   It finds one match, gives it to you, forgets it, and looks for the next one. It uses almost zero memory.

# Simulate a massive string (don't print this!)
massive_log = "Error: 404 " * 1000000

# BAD (Memory Spike):
# list_of_errors = re.findall(r"Error: \d+", massive_log)

# GOOD (Streamlined):
count = 0
for match in re.finditer(r"Error: \d+", massive_log):
    # 'match' is a Match Object, so we use .group()
    # We process it, then it is discarded from RAM.
    current_error = match.group()
    count += 1

print(f"Processed {count} errors efficiently.")

# Compilation (re.compile)
# If you are using the same pattern inside a loop (running it millions of times), compile it first.

# 1. Compile the pattern once (Prepare the robot)
email_pattern = re.compile(r"\w+@\w+\.\w+")

user_inputs = ["user1@test.com", "not_an_email", "user2@test.com"]

# 2. Use the compiled object
for item in user_inputs:
    # We call .search() directly on the object
    if email_pattern.search(item):
        print(f"Valid: {item}")

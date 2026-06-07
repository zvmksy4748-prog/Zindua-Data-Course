import os

'''
title: Professional check for file existence
video: 
'''

if os.path.exists('mbox-short.txt'):
    print("System Ready: File detected.")
    print(f"File Size: {os.path.getsize('mbox-short.txt')} bytes")
else:
    print("Error: File not found.")
    print(f"Current Working Directory: {os.getcwd()}")

# The "File Handle"
# INDUSTRY STANDARD (Robust)
with open('mbox-short.txt', 'r', encoding='utf-8') as fhandd:
    data = fhandd.read()
    print(f"Read {len(data)} characters., '\n")

# The moment the indentation ends, Python automatically closes the file.
# Even if the 'print' statement crashes, the file is safely closed by the OS.

with open('mbox-short.txt', 'r', encoding='utf-8') as fhand:
    for line in fhand:
        print(line.strip())
        line = line.rstrip()

        # 1. GUARD: Filter for the anchor
        if not line.startswith('From '):
            continue

        # 2. LOCATE: Find the start and end of what you want
        at_position = line.find('@')
        space_after_at = line.find(' ', at_position)

        # 3. EXTRACT: Slice the string precisely
        # We slice from one character after the '@' up to the next space
        domain = line[at_position + 1: space_after_at]

        print(f"Extracted Domain: {domain}")


'''
# with open('mbox-short.txt', 'w', encoding='utf-8') as fhand: this will overwrite the file content
'''

with open('mbox-short.txt', 'a', encoding='utf-8') as fh: # this will append the file
    fh.write("\nFrom: samora.edu")

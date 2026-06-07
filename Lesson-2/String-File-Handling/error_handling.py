# Error Handling

import sys

fname = input("Enter the file name: ")

try:
    with open(fname, 'r', encoding='utf-8') as fhand:
        # We only try to read if the open succeeds
        count = 0
        for line in fhand:
            count += 1
        print(f"Successfully processed {count} lines.")

except FileNotFoundError:
    # Handle the error without crashing the program
    print(f"Error: The file '{fname}' does not exist. Please check the spelling.")
    sys.exit() # Cleanly terminates the script
except PermissionError:
    print(f"Error: You do not have permission to access '{fname}'.")
    sys.exit()
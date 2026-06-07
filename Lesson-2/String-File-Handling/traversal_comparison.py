# Traversal Comparison Membership

'''
Traversal is the act of visiting every character in a sequence, one by one, to perform an operation.
In Python, this is the foundation of data processing, search algorithms, and text transformation.
The while loop is an "explicit" traversal. It requires you to manage the state of the loop manually.
'''

# Manual Traversal
fruit = 'banana'
index = 0

while index < len(fruit):
    char = fruit[index]
    print(f"Index {index} contains: {char}")
    index += 1

# Automatic Traversal:
for idx, char in enumerate(fruit):
    print(f"Index {idx} contains: {char}")

# Computational Patterns & String Logic - We use it to quantify data within a string.
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# Membership: The in Operator
# Character check
print('a' in 'banana') # True

# Substring check
print('nan' in 'banana') # True
print('z' in 'banana') # False
# Practical Use Case: Filtering data. if "http" in user_input: print("URL detected")

# String Comparison
choice = input("Enter 'yes' or 'no': ").lower().strip()

if choice == "yes":
    print("Proceeding...")
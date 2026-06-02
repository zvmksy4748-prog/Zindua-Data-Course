# User-Defined Functions: blocks of code you design, name, and reuse to solve your specific problems.

# 1. Python reads this and "saves" it for later. It does NOT print.
def cook_breakfast():
    print("Frying eggs...")
    print("Toasting bread...")

# 2. Execution starts here.
print("Step 1: Wake up")

# 3. Execution jumps to the 'cook_breakfast' block above.
cook_breakfast()

# 4. After finishing the function, execution jumps back here.
print("Step 3: Eat and go to work")
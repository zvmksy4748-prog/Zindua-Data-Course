# While Loop

n = 5
while n > 0:
    print(n)
    n = n - 1 # Updating the iteration variable
print('Blastoff!', '\n')

# Sometimes you want to stop a loop based on something that happens inside the body, rather than at the top.
# We use the break statement to immediately exit a loop.
# While break stops the entire loop, the continue statement only stops the current iteration.
# It tells Python: "Stop what you are doing in this round and jump back to the top of the loop to start the next round."

secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess < 0:
        print("Tyy again, Positive numbers only!")
        continue
    if guess == secret:
        print("You win!")
        break
    print("Try again...")
# Number Guessing Game
# Build a Guess the Number (with Difficulty Levels) Game

import os
import random

# File name where high scores will be saved
HIGH_SCORE_FILE = "high_scores.txt"


def load_leaderboard():
    """Loads high scores from the txt file and returns a sorted list of tuples."""
    leaderboard = []
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            for line in file:
                username, score = line.strip().split(",")
                leaderboard.append((username, int(score)))
    # Lower score (fewer attempts used) is better
    return sorted(leaderboard, key=lambda x: x[1])

def save_score(username, score):
    """Saves a new high score to the text file."""
    with open(HIGH_SCORE_FILE, "a") as file:
        file.write(f"{username},{score}\n")

def display_leaderboard():
    """Prints the top 5 players on the leaderboard."""
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("No high scores recorded yet.")
    else:
        print("High Score List (Top 5)")
        for index, (name, score) in enumerate(leaderboard[:5], 1):
            print(f"{index}. {name} - {score} tries")
    print("-------------------------------\n")

def give_hint(secret_number):
    """Generates a dynamic hint when the user struggles."""
    hints = []
    # Check divisibility
    for divisor in [2, 3, 5, 10]:
        if secret_number % divisor == 0:
            hints.append(f"divisible by {divisor}")

    if not hints:
        hints.append("a prime number" if secret_number > 1 else "an odd number")

    # Pick a random descriptive hint from valid attributes
    chosen_hint = random.choice(hints)
    print(f"HINT: The secret number is {chosen_hint}!")

def display_welcome():
    """Prints the welcome message."""
    print("-" * 35)
    print("Welcome To Number Guessing Game!")
    print("-" * 35 )
    display_leaderboard()  # Display current top scores before playing

def play_game():
    # Get user name for leaderboard tracking
    username = input("Enter your username: ").strip()
    if not username:
        username = "Anonymous"

    # Step 1: Choose Difficulty Level
    print("Choose your difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    while True:
        choice = input("Select level (1, 2, or 3): ").strip()
        if choice == "1":
            max_attempts = 10
            break
        elif choice == "2":
            max_attempts = 7
            break
        elif choice == "3":
            max_attempts = 5
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

    # Step 2: Generate random target number
    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"\nPick a number between 1 and 100.")
    print(f"You have {max_attempts} attempts left. Good luck!\n")

    # Step 3: Core Game Loop
    while attempts < max_attempts:
        remaining_guesses = max_attempts - attempts
        print(f"Attempts left: {remaining_guesses}")

        # Input validation block
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("That is not a valid integer. Try entering a number.\n")
            continue

        attempts += 1

        # Check guess evaluations
        if guess == secret_number:
            print(f"\n CONGRATULATIONS, {username}!")
            print(f"You correctly guessed {secret_number} in {attempts} tries!")
            print("Thanks for playing! Goodbye.")
            save_score(username, attempts)
            display_leaderboard()
            return
        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Too High!")

        # Step 4: Extension Feature - Give hint after exactly 3 wrong tries
        if attempts == 3 and secret_number != guess:
            give_hint(secret_number)

        print("-" * 30)

    # Triggered if loop finishes without breaking (attempts run out)
    print(f"\nGAME OVER! You ran out of attempts.")
    print(f"The correct number was: {secret_number}\n")
    print("Thanks for playing! Goodbye.")

def main ():
    display_welcome()
    play_game()
    display_leaderboard()  # Display current top scores after playing
    replay = input("Do you want to play again? (yes/no): ").lower().strip()
    if replay not in ["y", "yes"]:
        print("\nThanks for playing! Goodbye.")
    else:
        play_game()
        display_leaderboard()  # Display current top scores after playing
main()

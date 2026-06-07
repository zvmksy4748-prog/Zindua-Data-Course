# CLI Quiz Game Application
# Build an interactive quiz app that runs in the terminal and scores users based on correct answers.

import random
import time

question_bank = {
    "General Knowledge": [
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "correct": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "correct": "D"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "choices": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
            "correct": "C"
        },
        {
            "question": "What is the capital of France?",
            "choices": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "correct": "C",
        }
    ],
    "History": [
        {
            "question": "Who was the first President of the United States?",
            "choices": ["A. Thomas Jefferson", "B. Abraham Lincoln", "C. George Washington", "D. John Adams"],
            "correct": "C"
        },
        {
            "question": "In which year did World War II end?",
            "choices": ["A. 1943", "B. 1945", "C. 1950", "D. 1939"],
            "correct": "B"
        }
    ],
    "Math": [
        {
            "question": "What is the square root of 64?",
            "choices": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "correct": "C"
        },
        {
            "question": "What is 15 multiplied by 4?",
            "choices": ["A. 50", "B. 55", "C. 60", "D. 65"],
            "correct": "C"
        }
    ]
}

def display_welcome():
    """Prints the welcome message."""
    print("-" * 50)
    print("\t\t WELCOME TO INTERACTIVE QUIZ!")
    print("-" * 50 + "\n")


def select_category():
    """Allows the user to select a quiz category with input validation."""
    categories = list(question_bank.keys())

    while True:
        print("Available Categories:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")

        try:
            choice = int(input("\nChoose a category number: ").strip())
            if 1 <= choice <= len(categories):
                selected = categories[choice - 1]
                print(f"\nYou selected: {selected}\n" + "-" * 30)
                return selected
            else:
                print("⚠️ Invalid number. Please pick one from the list.\n")
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid integer.\n")


def run_quiz(questions, time_limit=10):
    """Main game loop managing question generation, timers, and scoring."""
    score = 0
    total_questions = len(questions)

    # Feature: Randomly shuffle the question order
    random.shuffle(questions)

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx} of {total_questions}:")
        print(q["question"])
        for choice in q["choices"]:
            print(choice)

        # Start the countdown timer
        start_time = time.time()

        # Feature: Input verification using try/except & condition tracking
        while True:
            try:
                user_input = input("\nYour Answer (A/B/C/D): ").strip().upper()
                end_time = time.time()
                elapsed_time = end_time - start_time

                # Check if the player ran out of time
                if elapsed_time > time_limit:
                    print(f"⏰ Time's up! You took {elapsed_time:.1f} seconds (Limit: {time_limit}s).")
                    print(f"The correct answer was {q['correct']}.")
                    break

                # Validate selection choice
                if user_input not in ["A", "B", "C", "D"]:
                    raise ValueError("Please enter only A, B, C, or D.")

                # Check correctness using branching if statements
                if user_input == q["correct"]:
                    print(f"✅ Correct! (Time taken: {elapsed_time:.1f}s)")
                    score += 1
                else:
                    print(f"❌ Wrong! The correct answer was {q['correct']}.")
                break

            except ValueError as e:
                print(f"⚠️ {e}")

    return score, total_questions


def display_feedback(score, total):
    """Calculates performance percentage and gives dynamic final feedback."""
    percentage = (score / total) * 100
    print("\n" + "-" * 50)
    print(f"Your Final Score: {score}/{total} ({percentage:.1f}%)")

    if percentage == 100:
        print("🏆 Excellent! Perfect score!")
    elif percentage >= 70:
        print("👍 Good job! You know your stuff.")
    else:
        print("Try Again! Practice makes perfect.")


def main():
    display_welcome()
    category = select_category()

    # Create a copy of the list so the original template remains unmodified
    questions = list(question_bank[category])

    score, total = run_quiz(questions)
    display_feedback(score, total)



main()
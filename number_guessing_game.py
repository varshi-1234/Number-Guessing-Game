import random

def get_attempts_from_difficulty(choice):
    if choice == "1":
        return 10, "Easy"
    elif choice == "2":
        return 5, "Medium"
    elif choice == "3":
        return 3, "Hard"
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        return 5, "Medium"

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")  # Default message

    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    choice = input("\nEnter your choice: ").strip()
    attempts, level_name = get_attempts_from_difficulty(choice)

    print(f"\nGreat! You have selected the {level_name} difficulty level.")
    print("Let's start the game!\n")

    number_to_guess = random.randint(1, 100)
    attempt_count = 0

    while attempt_count < attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempt_count += 1

            if guess == number_to_guess:
                print(f"Congratulations! You guessed the correct number in {attempt_count} attempts.")
                return
            elif guess < number_to_guess:
                print(f"Incorrect! The number is greater than {guess}.\n")
            else:
                print(f"Incorrect! The number is less than {guess}.\n")

        except ValueError:
            print("Please enter a valid number.\n")

    print(f"Sorry! You've used all your chances. The correct number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()

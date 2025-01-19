import random

def display_heading():
    print("============================")
    print("      GUESS THE NUMBER")
    print("============================")

def play_game(limit):
    number_to_guess = random.randint(1, limit)
    print(f"I'm thinking of a number between 1 and {limit}. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed it!")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    display_heading()
    while True:
        try:
            limit = int(input("Enter the limit for the number range: "))
            play_game(limit)
            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("Thanks for playing! Goodbye!")
                break
        except ValueError:
            print("Please enter a valid number for the limit. ")

if __name__ == "__main__":
    main()


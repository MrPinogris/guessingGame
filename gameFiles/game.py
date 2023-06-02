# game.py
import random

class Game:
    def __init__(self):
        self.secret_number = None
        self.number_of_guesses = 0
        # Add more member variables as needed

    def start(self):
        self.initialize()

        # Game loop
        while True:
            guess = self.get_user_guess()

            if guess == self.secret_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Wrong guess. Try again!")
                self.number_of_guesses += 1
                # Provide additional feedback or hints if needed

        # Display game statistics or perform other actions after the game ends

    def initialize(self):
        # Initialize the game by generating a secret number, resetting the number of guesses, etc.
        self.secret_number = random.randint(1, 100)
        self.number_of_guesses = 0

    def get_user_guess(self):
        # Accept user input for the guess and return the entered number
        while True:
            try:
                guess = int(input("Enter your guess: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

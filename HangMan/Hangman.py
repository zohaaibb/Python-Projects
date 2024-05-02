import random

print(" Welcome to Hangman ")
from Stages import logo
print(logo)  # Print the hangman logo

from words import word_list  # importing words from words.py
random_word = random.choice(word_list)  # Choose a random word to guess

# Print(f" {random_word}") You can run this to figure out what word is getting selected

display = []  # creating an empty list
for letter in range(len(random_word)):
    display += "_"  # Initialize display with underscores for each letter
print(display)

is_game_over = False  # creating a bool variable for ending game
lives = 6
while not is_game_over:
    guess = input(" Guess a letter: ").lower()  # Get user's guess and convert to lowercase
    for position in range(len(random_word)):  # Check if the guess is in the word
        word = random_word[position]
        if word == guess:
            display[position] = guess  # Update display with the guessed letter

    if guess not in random_word:  # If the guess is not in the word (fix the typo)
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            is_game_over = True
            print(" You Lose!")

    print(f"{' '.join(display)}")  # Print the updated display of guessed letters and underscores

    # Check for win condition (all letters guessed)
    if "_" not in display:
        is_game_over = True
        print(" You Won!")

    # Print the corresponding hangman stage based on remaining lives
    from Stages import stages
    print(stages[lives])

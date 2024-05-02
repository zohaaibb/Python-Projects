import random

print(" Welcome to Hangman ")
from Stages import logo
print(logo)
from words import word_list
random_name = random.choice(word_list)
#print(f" {random_name}")
display = []
for letter in range(len(random_name)):
    display += "_"
print(display)
is_game_over = False
lives = 6
while not is_game_over:
    guess = input(" Guess a letter: ").lower()
    for position in range(len(random_name)):
        word = random_name[position]
        if word == guess:
            display[position] = guess

    if word not in guess:
        lives -= 1
        if lives == 0:
            is_game_over = True
            print(" You Lose!")

    print(display)

    if "_" not in display:
        is_game_over = True
        print(" You Won!")
    from Stages import stages
    print(stages[lives])

import random
from art import logo,vs
print("================================")
print("***  Welcome To Higher Lower ***")
print("================================")

from game_data import data
print(logo)

def check_answer(guess, follower_a, follower_b):
    """Function to check the answers """
    if follower_a > follower_b:
        #will return true if a has more followers than b and user has guessed a
        return guess == "a"
    else:
        #will return true if b has more followers than a and user has guessed b
        return guess == "b"

def format_data(account):
    """Formats the data into printable format"""

    #fetching the required values using the keys from the Dictionary
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_desc} from {account_country}"

score = 0
is_game_on = False
#Generating random account from dictionary
account_b = random.choice(data)
while not is_game_on:
    
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f" Compare A: {format_data(account_a)}\n")
    print(f"{vs}\n")
    print(f" Compare B: {format_data(account_b)}\n")

    guess = input(" Who has more followers? Type 'A' or 'B' : \n").lower()

    #fetching followers count from the dictionary
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f" You're Right!: Your Current Score {score}\n")
    else:
        is_game_on = True
        print(f" You're Wrong!: Your Final Score {score}\n")
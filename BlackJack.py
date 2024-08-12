import random

print(" ******************************")
print(" *** Welcome to PYBlackJack ***")
print(" ******************************")

def deal_card():

    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    """Takes a list of cards and return their sum """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    """If there is 11 in card then it gets 
    removed and 1 is added in the list """

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    """Returning the sum of cards 
    by calling the sum function"""
    return sum(cards)


def compare(user_sc, computer_sc):
    if user_sc == computer_sc:
        return "Draw😑"
    elif computer_sc == 0:
        return "Lose, Opponent has a BlackJack🙂"
    elif user_sc == 0:
        return "Win with a BlackJack😎"
    elif user_sc > 21:
        return "You went over 😭"
    elif computer_sc > 21:
        return " Opponent went over , You Win!😃"
    elif user_sc > computer_sc:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_card = []  #Created an empty list to append user cards later
    computer_card = [] #Created an empty list to append computer cards 
    is_game_end = False


#Running the for loop twice so that 2 cards gets  added in the lists 
    for _ in range(2):
        """By Doing this the way below we would get same 
            cards for both computer and user 
        new_card = deal_card()
        user_card.append(new_card)
        computer_card.append(new_card)
    print(user_card)
    print(computer_card)
    
    So to not get same card we will do the choice given below"""

        user_card.append(deal_card())
        computer_card.append(deal_card())
    """
    print(computer_card)
    print(user_card)"""
    while not is_game_end:

        """Calculating Computer Score and User Score """
        computer_score = calculate_score(computer_card)
        user_score = calculate_score(user_card)


        """Letting the user know about his cards and score and the first card of Computer"""
        print(f" Your Cards:{user_card}, Your Score: {user_score}")
        print(f" Computer's First Card: {computer_card[0]}")

        """The Game ends if user score, computer score equals to 0 
        or user score is greater than 21 the game ends """
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_end = True
        else:
            """Asking the user if the user wants to draw another card"""
            choice = input(" Enter Y to draw a new card, Type n to pass: ")

            """If user draws another card then a card will be added to user cards 
            and its sum will be calculated otherwise game ends"""
            if choice == "y":
                user_card.append(deal_card())
            else:
                is_game_end = True

    """Checking until computer score is not equal to zero 
    and is less than 17 computer cards gets called and its
    score gets calculated"""

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f" Your Cards {user_card}, Your Score: {user_score}")
    print(f" Computer Cards {computer_card}, Computer Score: {computer_score}")

    """Calling the compare function and printing it """

    print(compare(user_score, computer_score))


"""Calling the function """
play_game()


"""Asking whether user wants to play again 
or not and calling the function"""

while input(" Do You want to Play The Game Again Type y or n ") == "y":
        play_game()
else:
    is_game_end = True
    

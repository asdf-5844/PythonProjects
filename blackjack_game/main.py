# A game of Blackjack that I probably already forgot how to play

import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards) # Random card

def calculate_score(cards):
    # If Blackjack (2 cards that add up to 21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Ace can either be 11 or 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    # Compares the user score u_score against the computer score c_score.
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    # Each player starts with two random cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        # Can only see the computer's first card
        print(f"Computer's first card: {computer_cards[0]}")
        # Game ends if...
        if user_score > 21 or user_score == 0 or computer_score == 0:
            game_over = True
        else:
            # User can choose to get a new card
            get_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_new_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    # Computer keeps getting new cards while no Blackjack and score under 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        print("\n" * 20)
        game()
    else:
        break

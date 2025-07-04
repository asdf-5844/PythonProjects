# Note: For this project give yourself plenty of comments
# To break large problems into smaller pieces

# Import
import art
import random
from game_data import data

print(art.logo)

def format_data(account):
    # Takes the account data and returns the printable format.
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, p1, p2):
    # Get follower count
    a_followers = p1["follower_count"]
    b_followers = p2["follower_count"]
    if a_followers > b_followers:
        # Returns a boolean
        return user_guess == "a"
    else:
        # True or False
        return user_guess == "b"

game_over = False
current_score = 0
person_b_index = random.choice(data)

while not game_over:
    # Making account at position B become the next account at position A.
    person_a_index = person_b_index
    person_b_index = random.choice(data)
    
    # When compares two of the same people
    if person_a_index == person_b_index:
        person_b_index = random.choice(data)
    
    # Game
    print(f"Compare A: {format_data(person_a_index)}")
    print(art.vs)
    print(f"Compare B: {format_data(person_b_index)}")
    ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Clear the screen
    print("\n" * 20)
    print(art.logo)
    
    # "check" is a boolean, True is correct, False is wrong
    check = check_answer(ans, person_a_index, person_b_index)
    if check:
        current_score += 1
        print(f"You're Right! Current Score {current_score}")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {current_score}")

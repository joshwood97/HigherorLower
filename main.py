# Generate random art 
print("Welcome to Higher or Lower.")
from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
    """Takes the user account and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and followers and returns if answer is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Make the game repeatable
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(date)
while game_should_continue:

    # Generate a random account from the game data.
    # Make account at position B become position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    # Ask the user for a guess
    guess = input("Who has more followers? Type A or B: ").lower()

    # Check if the user is correct 
    ## Obtain the follower accounts for each account 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count) 
    # Clear the screen between rounds
    clear()
    print(logo)

    # Give the user feedback based on their guess
    # Score keeeping 
    if is_correct:
        score += 1
        print(f"You're right!: Current Score is {score}")
    else: 
        game_should_continue = False
        print(f"Sorry, that's wrong: Final Score is {score}")


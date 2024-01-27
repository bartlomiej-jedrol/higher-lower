import art
import os
import random
from game_data import data

def print_comparison(profile_A, profile_B):
    """Prints data of Instagram profiles for a comparison."""
    print("Compare A: " + profile_A.get("name", "") + ", a " + profile_A.get("description", "") + ", from " + profile_A.get("country") + ".")
    print(art.vs)
    print("Against B: " + profile_B.get("name", "") + ", a " + profile_B.get("description", "") + ", from " + profile_B.get("country") + "." + "\n")

def check_if_guess(profile_A, profile_B, guess):
    """Compares follower count for given Instagram profiles. Returns if the user has guessed or not."""
    if profile_A.get("follower_count", 0) > profile_B.get("follower_count", 0):
        answer = "a"
    else:
        answer = "b"

    if answer == guess:
        return True
    else:
        return False

def play_game():
    """Plays a game."""
    print(art.logo)
    
    is_guess = True # Assign an initial value to enter the while loop.
    score = 0
    while is_guess:
        # Choose two random profiles from the data set.
        profile_A = random.choice(data)
        profile_B = random.choice(data)

        print_comparison(profile_A, profile_B)

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_guess = check_if_guess(profile_A, profile_B, guess)

        # Clear the console before printing the result.
        os.system("clear")
        print(art.logo)

        if is_guess:
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.\n")

while input("Do you want to play the Higher Lower game? Type 'y' or 'n': ").lower() == "y":
    os.system("clear")
    play_game()

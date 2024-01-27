"""Module contains code for the Higher Lower game."""
import os
import random
from game_data import data
from art import logo, vs

def get_random_profile():
    """Returns a random profile from a data set."""
    return random.choice(data)

def format_data(profile):
    """Returns the Instagram profile data for a comparison 
    in a readable format: name, description, and country."""
    name = profile.get("name", "")
    description = profile.get("description", "")
    country = profile.get("country", "")

    return f"{name}, a {description}, from {country}."

def check_answer(profile_a, profile_b, guess):
    """Compares follower count for given Instagram profiles. 
    Returns the result of guessing."""
    if profile_a.get("follower_count", 0) > profile_b.get("follower_count", 0):
        answer = "a"
    else:
        answer = "b"

    return answer == guess

def play_game():
    """Plays a game."""
    print(logo)
    game_should_continue = True
    score = 0
    profile_a = get_random_profile()
    profile_b = get_random_profile()

    while game_should_continue:
        profile_a = profile_b
        # For a subsequent attempts the user continue
        # with one of the profiles from a previous attempt.
        profile_b = get_random_profile()

        # Exclude the comparison between the same profiles.
        while profile_a == profile_b:
            profile_b = get_random_profile()

        print(f"Compare A: {format_data(profile_a)}")
        print(vs)
        print(f"Compare B: {format_data(profile_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        # The game should continue if the user is correct.
        game_should_continue = check_answer(profile_a, profile_b, guess)
              
        # Clear the console before printing the result.
        os.system("clear")
        print(logo)

        if game_should_continue:
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.\n")

while input("Do you want to play the Higher Lower game? Type 'y' or 'n': ").lower() == "y":
    os.system("clear")
    play_game()

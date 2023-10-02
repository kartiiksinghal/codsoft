#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("------------------------Codsoft Task-3------------------------")
print("ROCK-PAPER-SCISSORS GAME")

import random

# Function to determine the winner of a round
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (user_choice == "r" and bot_choice == "s") or \
         (user_choice == "s" and bot_choice == "p") or \
         (user_choice == "p" and bot_choice == "r"):
        return "You win!"
    else:
        return "Computer wins!"

# Initializing scores
user_score = 0
bot_score = 0

# Main loop
while True:
    
    # Asking user to choose rock (r), paper (p), or scissors (s)
    user_choice = input("Choose (r/p/s): ").lower()
    
    # Validating user input
    if user_choice not in ["r", "p", "s"]:
        print("Invalid choice. Please choose (r) for rock, (p) for paper, or (s) for scissors.")
        continue
    
    # Generating random choice for computer
    choices = ["r", "p", "s"]
    bot_choice = random.choice(choices)
    
    # Determine the winner and display the result
    result = determine_winner(user_choice, bot_choice)
    print(f"You chose {user_choice}. Computer chose {bot_choice}.")
    print(result)
    
    # Update scorecard
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        bot_score += 1
    
    # Display current scores
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {bot_score}")
    
    # Asking if user wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


# In[ ]:





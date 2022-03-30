# Importing the libraries 
import random 

# Creating the game system
def play():
    user = input("What you chose? 'r' for rock, 'p' for paper and 's' for sissors \n")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return "tie"
    if win_condition(user, computer):
        win = print(f"{user} x {computer} \n You won! \n")
        return win
    lost = print(f"{user} x {computer} \n You lost! \n")
    return lost

# Setting the game win condition rules
def win_condition(player, opponent):
    # r> s; s> p; p> r.
    if (player == 'r' and opponent == 's') or (player == 's' and opponent =='p') or (player == 'p' and opponent == 'r'):
        return True
play()
# Importing the libraries
import random


# The introduction for the user
print("************************")
print("      Guess Game         ")
print("************************")
nick = input(f"Hey, whats your name?\n")

# The endgame image
def win():
    print("************************")
    print("      You won!         ")
    print("************************")
def lose():
    print("************************")
    print("      You lost!         ")
    print("************************")

# Creating the difficulty sistem
dif = int(input(f"Now, {nick}, choose one of these difficulties: \n 1: Easy; \n 2: Moderate \n 3: Hard\n"))
value = dif * 10
tries = int(10 / dif)
# Creating the loop and the game system
def guess(value, tries):
    random_number = random.randint(1, value)
    guess = 0
    while guess != random_number and tries != 0:
        guess = int(input("What number you choose?"))
        if guess > random_number:
            print("This is a really high value, try again.")
            tries = tries -1
            print(f"You have {tries} left")
        elif guess <random_number:
            print("Try an big one.")
            tries = tries -1
            print(f"You have {tries} left")
    if tries == 0:
        lose()
        print(f"The number was {random_number}!")
    elif tries > 0:
        win()
        print(f"The number was {random_number}!")

# Getting the game working:
=======
# Importing the libraries
import random



# The introduction for the user
print("************************")
print("      Guess Game         ")
print("************************")
nick = input(f"Hey, whats your name?\n")

# The endgame image
def win():
    print("************************")
    print("      You won!         ")
    print("************************")
def lose():
    print("************************")
    print("      You lost!         ")
    print("************************")

# Creating the difficulty sistem
dif = int(input(f"Now, {nick}, choose one of these difficulties: \n 1: Easy; \n 2: Moderate \n 3: Hard\n"))
value = dif * 10
tries = int(10 / dif)
# Creating the loop and the game system
def guess(value, tries):
    random_number = random.randint(1, value)
    guess = 0
    while guess != random_number and tries != 0:
        guess = int(input("What number you choose?"))
        if guess > random_number:
            print("This is a really high value, try again.")
            tries = tries -1
            print(f"You have {tries} left")
        elif guess <random_number:
            print("Try an big one.")
            tries = tries -1
            print(f"You have {tries} left")
    if tries == 0:
        lose()
        print(f"The number was {random_number}!")
    elif tries > 0:
        win()
        print(f"The number was {random_number}!")

# Getting the game working:
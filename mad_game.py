from time import sleep
# The welcome page
def welcome():
    print("=======================")
    print("        MadGame        ")
    print("=======================")
    sleep(2)
# The game system
def jogar():
    welcome()
    print("Now, we will ask you some types of words that you can choose to create the mad phrase.")
    sleep(2)
    # Creating the variables
    adj1 = input("Choose an adjetive")
    adj2 = input("Another one")
    noum = input("Choose a noum")
    verb = input("Choose a verb")

    # Building the phrase
    print(f"The world would be better if you were more {adj1}, actually, do you know that {noum} can {verb} video games? It's complicated to explain, but {noum} is {adj2}")
jogar()
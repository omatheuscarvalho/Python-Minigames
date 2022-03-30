from time import sleep

# Asking the 2 numbers
n1 = int(input("Whats the first number?"))
n2 = int(input("And the seccound one?"))

# The menu
option = 0
while option != 5:
    print('''
    [1] Sum;
    [2] Subtract;
    [3] Multiply;
    [4] Other numbers;
    [5] Close.
    ''')
    option = int(input(">>>>>>>>>>> Witch option you choose?"))
    
    #Defining the opperations
    if option == 1:
        sum = n1 + n2
        print(f"{n1} + {n2} = {sum}")
    elif option == 2:
        subtract = n1 - n2
        print(f"{n1} - {n2} = {subtract}")
    elif option == 3:
        multiply = n1 * n2
        print(f"{n1} x {n2} = {multiply}")
    elif option == 4:
        n1 = int(input("Whats the first number?"))
        n2 = int(input("And the seccound one?"))
    elif option == 5:
        print(">>>>>>>>>>> STOPPING")
    else:
        print(f"{option} is not an valid option, try again.")
    sleep(1)

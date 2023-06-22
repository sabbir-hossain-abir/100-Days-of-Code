print('''
| _____ |   | ___ | ___ ___ | |   | |
| |   | |_| |__ | |_| __|____ | | | |
| | | |_________|__ |______ |___|_| |
| |_|   | _______ |______ |   | ____|
| ___ | |____ | |______ | |_| |____ |
|___|_|____ | |   ___ | |________ | |
|   ________| | |__ | |______ | | | |
| | | ________| | __|____ | | | __| |
|_| |__ |   | __|__ | ____| | |_| __|
|   ____| | |____ | |__ |   |__ |__ |
| |_______|_______|___|___|___|_____|
''')

print("Welcome to treasure Island!")
print("Your mission is to steal the art from the island")

move1 = input('You\'re at a crossroad. Where do you want to go? type "left" or "right" ')
move1_l = move1.lower()

if move1_l == "right":
    print("You are dead")
else:
    print("You survived")

    move2 = input('You came to a river. Do you want to wait for the boat or swim? Type "Swim" or "Wait" ')
    move2_l = move2.lower()
    if move2_l == "swim":
        print("You're drowned to death")
    else:
        print("You have crossed the river")

        move3 = input("There is a house with 3 doors. Which door do you want to go in? Red/Blue/Yellow ")
        move3_l = move3.lower()
        if move3_l == "red" or move3_l == "blue":
            print("Game over")
        else:
            print("You win")

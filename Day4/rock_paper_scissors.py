import random

players_move = int(input("What move do you want to make? Type 0 for Rock, type 1 for paper, type 2 for scissors: "))

computers_move = random.randint(0,2)

print(f"Computer chose: {computers_move}")

if players_move == 0 and computers_move == 1:
    print("Computer Wins")
elif players_move == 0 and computers_move == 2:
    print("Computer win")
elif players_move == 1 and computers_move == 0:
    print("Player Wins")
elif players_move == 1 and computers_move == 2:
    print("Computer wins")
elif players_move == 2 and computers_move == 0:
    print("Computer Wins")
elif players_move == 2 and computers_move == 1:
    print("Player Wins")
else:
    print("Draw")

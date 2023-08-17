import random
import math
import numbers

# draw board function

def printboard(gamespace):
    print(" " + gamespace[0] + " | " + gamespace[1] + " | " + gamespace[2] + " ")
    print("___|___|___")
    print(" " + gamespace[3] + " | " + gamespace[4] + " | " + gamespace[5] + " ")
    print("___|___|___")
    print(" " + gamespace[6] + " | " + gamespace[7] + " | " + gamespace[8] + " ")
    print("   |   |   ")


# picking your piece

gamespace = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
user = input("Would you like to play as X or O? ")
user = user.upper()
gameEnd = False

while (user != "X") and (user != "O"):
    user = input("Let's try picking X or O this time! ")
    user = user.upper()

if user == "X":
    com = "O"
else:
    com = "X"

print("Alright! You'll be " + user + ", and I'll be " + com + "!")

# drawing out the board

printboard(gamespace)

while not gameEnd:


    position = input("Where would you like to go? (imagine each space as a number on a keypad) ")
    position = int(position)

    while (position <= 0) and (position > 9):
        position = input("Hey! Pick a valid number! ")
        position = int(position)

    gamespace[position - 1] = user

    printboard(gamespace)

    
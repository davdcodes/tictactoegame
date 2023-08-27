import random
import math
import numbers

# draw board function

def printboard(gamespace):
    print()
    print(" " + gamespace[0] + " | " + gamespace[1] + " | " + gamespace[2] + " ")
    print("___|___|___")
    print(" " + gamespace[3] + " | " + gamespace[4] + " | " + gamespace[5] + " ")
    print("___|___|___")
    print(" " + gamespace[6] + " | " + gamespace[7] + " | " + gamespace[8] + " ")
    print("   |   |   ")
    print()


# check win cons

def gameEnd(gamespace, user):
    if not ((gamespace[1] != " ") and (gamespace[3] != " ") and (gamespace[4] != " ") and (gamespace[5] != " ") and (gamespace[7] != " ")):
        if (gamespace[0] == user) and (gamespace[0] == gamespace[1]) and (gamespace[0] == gamespace[2]):   # top 
            return True
        elif (gamespace[3] == user) and (gamespace[3] == gamespace[4]) and (gamespace[3] == gamespace[5]): # mid hori 
            return True
        elif (gamespace[6] == user) and (gamespace[6] == gamespace[7]) and (gamespace[6] == gamespace[8]): # bottom 
            return True
        elif (gamespace[0] == user) and (gamespace[0] == gamespace[3]) and (gamespace[0] == gamespace[6]): # left 
            return True
        elif (gamespace[1] == user) and (gamespace[1] == gamespace[4]) and (gamespace[1] == gamespace[7]): # mid vert 
            return True
        elif (gamespace[2] == user) and (gamespace[2] == gamespace[5]) and (gamespace[2] == gamespace[8]): # right 
            return True
        elif (gamespace[0] == user) and (gamespace[0] == gamespace[4]) and (gamespace[0] == gamespace[8]): # top left 
            return True
        elif (gamespace[2] == user) and (gamespace[2] == gamespace[4]) and (gamespace[2] == gamespace[6]): # top right 
            return True
        
    return False

replay = "y"

print("Welcome to the Tic Tac Toe Game! I'll try and go easy on you, so good luck!")
print()

while replay == "y":

    # picking your piece

    gamespace = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    user = input("Would you like to play as X or O? ")
    user = user.upper()
    gameOver = False

    while (user != "X") and (user != "O"):
        user = input("Let's try picking X or O this time! ")
        user = user.upper()

    if user == "X":
        com = "O"
    else:
        com = "X"

    print("Alright! You'll be " + user + ", and I'll be " + com + "!")

    if user == "X":
        playerTurn = True
    else:
        playerTurn = False

    printboard(gamespace)

    while not gameOver:

        # check if COM's turn or not

        if playerTurn == True:

            # check if input is a number, then if in range, then turns into a number and places it if true   

            position = input("Where would you like to go? (imagine each space as a number on a keypad) ")
            while (str(position).isnumeric() == False) or ((int(position) <= 0) or (int(position) > 9)):
                if str(position).isnumeric() == False:
                    position = input("Hey, let's try entering a valid number this time! ")
                else:
                    position = int(position)
                    if position < 1 or position > 9:
                        position = input("Hey, pick a number that fits onto the keypad! ")
            position = int(position)

            gamespace[position - 1] = user

            printboard(gamespace) 

            playerTurn = False

            gameOver = gameEnd(gamespace,user)

            if gameOver:
                print("Aw, Game Over. You win.")
                break

        else:
            
            print("Hmmmm, oh! I'll go here!")

            choice = random.randint(0,8)
            while gamespace[choice] != " ":
                choice = random.randint(0,8)
            gamespace[choice] = com

            printboard(gamespace)

            playerTurn = True

            gameOver = gameEnd(gamespace,com)

            if gameOver:
                print("Game over! I win! Yipee!")
                break

        # check if game is over by fill

        if (not (" " in gamespace)) or gameOver:
            print("Game Over! We ran out of spaces!")
            print()
            gameOver = True

    replay = input("Would you like to play again? Enter 'y' to play again, or any other key to quit: ")
    print()

print("Thanks for playing!")
# Purpose: Two players or player vs computer take turns by adding numbers(1-10) starting from sum=0. First player who reaches 100 wins.
# Author: Youssef Amgad Abd Al Halim Ahmed


import random
import time
# function that displays status and chooses game-mode
def display():
    # Welcome message, display status and input player names
    print('Welcome to 100 Game')
    print('sum=0')
    print()
    # Choosing game-mode
    print('Please choose a Game-mode')
    print()
    print('A. Player vs computer')
    print('B. player vs player')
    print('Please enter A or B ')
    choice = input()
    # checking that the choice is correct
    while choice not in ["A", "B"]:
        print('Invalid, please enter A or B ')
        choice = input()
    return choice

def main():
    # setting sum to zero
    sum=0


    # setting bool flag to true
    flag=True

    # taking users choice from display function
    choice=display()

    if choice=="B":
        # inputting player names
        player1 = input('Please enter player1 name ')
        player2 = input('Please enter player2 name ')
        # Game playing
        while sum < 100:

            # Player 1 Turn
            print("It is", player1 + "'s", "turn")

            # Condition that checks if sum reached between 91 and 99 to force players to enter certain numbers so that the sum doesn't exceed 100
            if 90 < sum < 100:
                print(player1 + ',' + ' Please choose a number between 1 and', 10 - (sum % 10))
                flag = False

                move = input()
                while not move.isdigit():  # to check if entered input is an integer
                    print(player1 + ',' + ' Please enter a number from 1 to', 10 - (sum % 10))
                    move = input()
                move = int(move)

                while move < 1 or move > 10 - (sum % 10):
                    print(player1 + ',' + ' That is an Invalid number,Please enter a number from 1 to', 10 - (sum % 10))
                    move = input()
                    while not move.isdigit():  # to check if entered input is an integer
                        print(player1 + ',' + ' Please enter a number from 1 to', 10 - (sum % 10))
                        move = input()
                    move = int(move)

            # If sum didn't reach 91 then both players can enter a number between 1 and 10 normally
            if flag:
                print(player1 + ',' + ' Please enter a number from 1 to 10 ')
                move = input()
                while not move.isdigit():  # to check if entered input is an integer
                    print(player1 + ',' + ' Please enter a number from 1 to 10 ')
                    move = input()
                move = int(move)
                if move < 1 or move > 10:

                    while move < 1 or move > 10:  # checking validity of entered number
                        print(player1 + ',' + ' That is an Invalid number, please enter a number from 1 to 10 ')
                        move = input()
                        while not move.isdigit():  # to check if entered input is an integer
                            print(player1 + ',' + ' Please enter a number from 1 to 10 ')
                            move = input()
                        move = int(move)

            # Updating Status
            sum = sum + move
            print('Now the sum equals', sum)

            # checking if player 1 won
            if sum == 100:
                print(player1 + ',' + ' Congratulations! You are the winner')
                break

            # Player 2 Turn
            print("It is", player2 + "'s", "turn")

            # Condition that checks if sum reached between 91 and 99 to force players to enter certain numbers so that the sum doesn't exceed 100
            if 90 < sum < 100:
                print(player2 + ',' + ' Please choose a number between 1 and', 10 - (sum % 10))
                flag = False

                move = input()
                while not move.isdigit():
                    print(player2 + ',' + ' Please choose a number between 1 and', 10 - (sum % 10))
                    move = input()
                move = int(move)
                while move < 1 or move > 10 - (sum % 10):
                    print(player2 + ',' + ' That is an Invalid number,Please enter a number from 1 to', 10 - (sum % 10))
                    move = input()
                    while not move.isdigit():
                        print(player2 + ',' + ' Please choose a number between 1 and', 10 - (sum % 10))
                        move = input()
                    move = int(move)

            # If sum didn't reach 91 then both players can enter a number between 1 and 10 normally
            if flag:
                print(player2 + ',' + ' Please choose a number between 1 and 10 ')
                move = input()
                while not move.isdigit():
                    print(player2 + ',' + ' Please choose a number between 1 and 10 ')
                    move = input()
                move = int(move)
                if move < 1 or move > 10:

                    while move < 1 or move > 10:  # checking validity of entered number
                        print(player2 + ',' + ' That is an Invalid number, please enter a number from 1 to 10 ')
                        move = input()
                        while not move.isdigit():
                            print(player2 + ',' + ' Please choose a number between 1 and 10 ')
                            move = input()
                        move = int(move)

            # Updating Status
            sum = sum + move
            print('Now the sum equals', sum)

            # checking if player 2 won
            if sum == 100:
                print(player2 + ',' + ' Congratulations! You are the winner')
                break
    elif choice=="A":
        player1 = input("Please enter your name ")
        print(player1+','+ " you will play against Jarvis")
        print("Try to beat him")

        # Game playing
        while sum < 100:

            # Player 1 Turn
            print("It is", player1 + "'s", "turn")

            # Condition that checks if sum reached between 91 and 99 to force players to enter certain numbers so that the sum doesn't exceed 100
            if 90 < sum < 100:
                print(player1 + ',' + ' Please choose a number between 1 and', 10 - (sum % 10))
                flag = False

                move = input()
                while not move.isdigit():  # to check if entered input is an integer
                    print(player1 + ',' + ' Please enter a number from 1 to', 10 - (sum % 10))
                    move = input()
                move = int(move)

                while move < 1 or move > 10 - (sum % 10):
                    print(player1 + ',' + ' That is an Invalid number,Please enter a number from 1 to', 10 - (sum % 10))
                    move = input()
                    while not move.isdigit():  # to check if entered input is an integer
                        print(player1 + ',' + ' Please enter a number from 1 to', 10 - (sum % 10))
                        move = input()
                    move = int(move)

            # If sum didn't reach 91 then both players can enter a number between 1 and 10 normally
            if flag:
                print(player1 + ',' + ' Please enter a number from 1 to 10 ')
                move = input()
                while not move.isdigit():  # to check if entered input is an integer
                    print(player1 + ',' + ' Please enter a number from 1 to 10 ')
                    move = input()
                move = int(move)
                if move < 1 or move > 10:

                    while move < 1 or move > 10:  # checking validity of entered number
                        print(player1 + ',' + ' That is an Invalid number, please enter a number from 1 to 10 ')
                        move = input()
                        while not move.isdigit():  # to check if entered input is an integer
                            print(player1 + ',' + ' Please enter a number from 1 to 10 ')
                            move = input()
                        move = int(move)

            # Updating Status
            sum = sum + move
            print('Now the sum equals', sum)

            # checking if player 1 won
            if sum == 100:
                print(player1 + ',' + ' Congratulations! You are the winner')
                break

            # Jarvis Turn
            print("It is Jarvis's turn")

            # Condition that checks if sum reached between 91 and 99 to force players to enter certain numbers so that the sum doesn't exceed 100
            if 90 < sum < 100:
                flag=False
                move=random.randint(1,10-(sum %10))
                print("Jarvis chooses",move)


            # If sum didn't reach 91 then both players can enter a number between 1 and 10 normally
            if flag:
                move = random.randint(1, 10)
                print("Jarvis chooses", move)


            # Updating Status
            sum = sum + move
            print('Now the sum equals', sum)

            # checking if player 2 won
            if sum == 100:
                print("Jarvis wins!!!")
                print('Better luck next time',player1)
                break

    # checking if player wants to play again
    print("Thanks for playing, Would you like to play again?")
    print("Enter A if you want to play again")
    print("Enter B if you want exit")
    choice=input()
    while choice not in ["A", "B"]:
        print('Invalid, please enter A or B ')
        choice = input()
    if choice == "A":main()
    elif choice == "B":

        print("Thanks for playing our game")
        time.sleep(3.5)
        exit()


main()
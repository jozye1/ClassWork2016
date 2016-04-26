# Python Assignment 3.4 - Guessing Game
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier
# Date: 26 April 2016

def guessingGame():

    import random
    print("")
    global userInput
    userInput = 0
    #userInput = int(input("Please enter a guessed number between 1 and 10:  "))
    guessedNumber = random.randint(1, 10)
    #print(random.randint(1, 10))
    global count
    count = 0
    #counter = 0
    value = True
    while value == True:
        count += 1
        for guessed in range(count+1):
            print("")
            userInput = int(input("Please enter a guessed number between 1 and 10:  "))
            print("")

            if guessedNumber == userInput:
            #print(random.randint(1, 10))
                print("")
                print("WOW, Outstanding! You have guessed the random number correctly: ", guessedNumber)
                value = False

            elif userInput != guessedNumber or count != 3:
                count += 1
                print("Oh nooo, you almost had it! Please try again! You've got ", count, "more times to try.")
                print("")
            else:
                print("")
                print("It is too bad you could not guessed the right number.")
                print("The number needed to guess is: ", guessedNumber)
                value = False
                break
    print("")
    print("Thank you for having fun with us! Please come back again soon!")

guessingGame()

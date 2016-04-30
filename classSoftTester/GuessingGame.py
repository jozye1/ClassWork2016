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
    global count,counter
    count = 0
    counter = 3

    print("Welcome to our number-guessing game! You have three attempts at guessing the correct number.")

    value = True
    while value == True:
        count += 1
        for guessed in range(count):
            print("")
            userInput = int(input("Please enter a guessed number between 1 and 10:  "))
            print("")
            counter -= 1
            if guessedNumber == userInput:
            #print(random.randint(1, 10))
                print("")
                print("WOW, Outstanding! You have guessed the random number correctly, which is: ", guessedNumber)
                value = False
                break
            #elif userInput != guessedNumber:
                print("Oh nooo, you almost had it! Please try again! You've got ", counter, "more times to try.")
                print("")
            elif count == 3:
                print("Oh nooo, you almost had it! Please try again! You've got ", counter, "more times to try.")
                print("")
                print("counter proof: ", count)
                print("You have exhausted all your attempts. Please go home and think about it, or give us a call to reset your account.")
                value = False
                break
            else:
                print("")
                print("It is too bad you could not guessed the right number.")
                print("The number needed to guess is: ", guessedNumber)
                value = False
                break
    print("")
    print("Thank you for having stopped by & have fun with us! Please come back again soon!")

guessingGame()

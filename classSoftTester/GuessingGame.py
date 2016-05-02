# Python Assignment 3.4 - Guessing Game
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier
# Date: 26 April 2016

def guessingGame():

    import random
    global userInput
    userInput = int(0)
    guessedNumber = random.randint(1, 10)
    global counter
    #count = 0
    counter = 3

    print("")
    print("Welcome To Our Number-Guessing Game! You Have 3 Attempts At Guessing The Correct Number.")
    print("########################################################################################")
    #print("")

    value = True
    while value == True:
        #count += 1
        counter -= 1

        try:
            if counter >= 0:
                print("")
                userInput = int(input("Please enter a guessed number between 1 and 10: "))
                #userInput = int()
                #print("")
        except:
            if counter > 0 and counter < 3:
                print("")
                print("\tPlease, enter a valid integer value.")
                print("\tWhat must you be thinking about!? Vamonos ahora! Only", counter, "more time(s) left to try.")
                print("")

        if guessedNumber == userInput:
            print("")
            print("******************************************************************************************")
            print("WOW, Outstanding! You have guessed the random number correctly, which is: ", guessedNumber)
            print("")
            print("I, Josue, Thank you for having stopped by & have fun with us! Please come back again soon!")
            print("******************************************************************************************")
            print("")
            print("")
            goAgain = str(input("||Wish to go again? 'Y or y' to start over, or enter any other character to quit the game: "))
            print("============================================================================================")
            print("")
            if goAgain == "Y" or goAgain == "y":
                value = True
                counter = 3
                userInput = int()
            else:
                value = False
                return

        if (counter >= 2 and userInput < int(0)) or (userInput > int(10)):
            print("\tTime is not on your side - HURRY!")
        elif (counter >= 1 and userInput > int(10)) or (userInput < int(0)):
            print("\tI pity NOT the fool who does NOT follow instructions! Now you've got", counter, "egg left in your basket. Whatcha gonna do!?")

        if ((guessedNumber == userInput + 1) or (guessedNumber == userInput - 1)) and (userInput < 11 and userInput > -1):
            print("\tFolks, Is it Summer time already? It is so \"HOT\" in here! You've got", counter, "more time(s) to try.")
        elif ((guessedNumber == userInput + 2) or (guessedNumber == userInput - 2)) and (userInput < 11 and userInput > -1):
            print("\tThe temperature is sure rising up. It is quite \"WARM\" in this house...only", counter, "more attempt(s) left for you.")
        elif (userInput < 11 and userInput > 0) and (userInput != guessedNumber):
            print("\tIt is so \"COLD\" in the Winter time, specially in the North East. You've got", counter, "more time(s) to try.")


        if (userInput > int(10)) and (counter > 0):
            #print("")
            print("\tPlease enter a number that is not greater than 10.")
        elif (userInput < int(0)) and (counter > 0):
            #print("")
            print("\tPlease enter a number that is not less than 0.")


        if counter <= 0:
            print("")
            print("**************************************************************************************************************************************")
            print("It is too bad you could not guess the right number.")
            print("You have exhausted all of your attempts. Please go home and think about it, or give us a call to reset your account at: 800-try-again.")
            print("")
            print("The Number You Needed To Guess Is: ", guessedNumber)
            print("I, Josue, thank you for having stopped by & have fun with us! Please come back again soon!")
            print("**************************************************************************************************************************************")
            print("")
            print("")
            goAgain = str(input("||Wish to go again? 'Y or y' to start over or, enter any other character to quit the game: "))
            print("============================================================================================")
            if goAgain == "Y" or goAgain == "y":
                value = True
                counter = 3
                userInput = int()
            else:
                value = False
                return

guessingGame()

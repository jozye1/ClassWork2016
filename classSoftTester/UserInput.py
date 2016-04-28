# Python Assignment 3.3 - User Input
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier
# Date: 22 April 2016

def userInput():

    count = 0
    #global counter
    counter = 0
    enteredValues = []
    global iterationValue
    iterationValue = 0
    #value = True

    goodData = True
    while goodData == True:
        counter += 1
        try:
            print("")
            iterationValue = int(input("Please enter the number of times you wish to enter a value: "))
            count += 1
            goodData = False
        except:
            print("")
            print("This program only accepts numeric characters. ")
            if count == 0:
                counter = 3
                count = 1
                print("You have ", counter, " more chances to try again.")
            elif count == 1:
                counter = 2
                count = 2
                print("You have ", counter, " more chance to try again.")
            elif count == 2:
                print("1) We regret that you were not able to able to play & enjoy the game. Come back later.")
                break
                return


    if iterationValue <= 0:
        return

    while iterationValue >= 0:
        counter += 1
        try:
            print("")
            enteredValues.append(int(input("Please enter a number: ")))
            count += 1
            if iterationValue < count:
                break
        except:
            print("")
            print("This program only accepts numeric characters. ")
            if count == 0:
                counter = 3
                print("You have ",counter," more chances to try again.")
            elif count == 1:
                counter = 2
                print("You have ", counter, " more chance to try again.")
            elif count == 2:
                print("2) We regret that you were not able to able to play & enjoy the game. Come back later.")
                #value = False
                break

        #if iterationValue >= count or iterationValue == count or iterationValue < count:
            #value = False
                #return
        #goOn = str(input("Do you wish to continue? Enter 'Q' or 'q' to quit, otherwise enter any other character to continue: "))
        if iterationValue <= 0:
            #value = False
            return
        #else:
           # value = True
    print("")
    print("This is the list of entered numbers: ", end="")

    for enteredData in range(0, iterationValue):
        print(enteredValues[enteredData], end=" ")
    enteredValues.sort()
    print("")
    print(enteredValues)

    print("")

    print("The minimum or least number entered in the list is: ", enteredValues[0])
    print("The maximum or largest number entered in the list is: ", enteredValues[iterationValue -1])

userInput()

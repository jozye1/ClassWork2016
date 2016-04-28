# Python Assignment 3.3 - User Input
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier
# Date: 22 April 2016

def userInputMain():
    global iterationValue, goodData, enteredValues
    enteredValues = []
    iterationValue = 0
#userInputMain()

#def acceptableData():
    global count
    count = 0
    counter = 0
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
            if count == 1:
                counter = 3
                count = 2
                print("You have ", counter, " more chances to try again.")
            elif count == 2:
                counter = 2
                count = 3
                print("You have ", counter, " more chance to try again.")
            elif count == 3:
                print("1) We regret that you were not able to able to play & enjoy the game. Come back later.")
                break
                return

        if iterationValue <= 0:
            return
#acceptableData()

#def iterationCalculations():
    #global count
    count = 0
    counter = 0
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
            if count == 1:
                counter = 3
                print("You have ",counter," more chances to try again.")
            elif count == 2:
                counter = 2
                print("You have ", counter, " more chance to try again.")
            elif count == 3:
                print("2) We regret that you were not able to able to play & enjoy the game. Come back later.")
                break

        if iterationValue <= 0:
            return
#iterationCalculations()
userInputMain()

def printedResults():
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

printedResults()

def repeatingProcess():
    keepingGoing = True
    while keepingGoing == True:
        print("")
        goOn = str(input("Do you wish to continue? Enter 'Q' or 'q' to quit, otherwise enter any other character to continue: "))
        print("")
        if goOn == str("Q") or goOn == str("q"):
            goodData = False
            keepingGoing = False
            return
        else:
            goodData = True
            #acceptableData()
            #iterationCalculations()
            userInputMain()
            printedResults()
            #keepingGoing = True

repeatingProcess()

print("")
print("Thank you for taking part in our promotion! Please come back soon! Have a great day!!!")







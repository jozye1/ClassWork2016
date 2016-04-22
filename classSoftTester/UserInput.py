# Python Assignment 3.3 - User Input
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier

def userInput():

    count = 0

    print("")
    iterationValue = int(input("Please enter the number of times you wish to enter a value: "))
    enteredValues = []

    value = True
    while value == True:
        print("")
        enteredValues.append(int(input("Please enter an integer value: ")))
        count += 1
        #goOn = str(input("Do you wish to continue? Enter 'Q' or 'q' to quit, otherwise enter any other character to continue: "))
        if iterationValue < 1:
            value = False
            break
        else:
            value = True
    print("")
    print("This is the list of entered numbers: ", end="")
    #if count >= 0 and count < 1000:
    for enteredData in range(0, count):
        print(enteredValues[enteredData], end=" ")
        print("")

userInput()

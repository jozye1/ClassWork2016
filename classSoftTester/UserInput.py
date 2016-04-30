# Python Assignment 3.3 - User Input
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier
# Date: 22 April 2016

def userInput():

    global count
    count = 0

    iterationValue = 0
    print("")
    try:
        iterationValue = int(input("Please enter the number of times you wish to enter a value: "))
    except:
        print("Please enter a numeric value. ")
    #if iterationValue >= 0 and iterationValue.isnumeric() == True:
        iterationValue
    else:
        print("We regret that you did not wish to play today. Please take a rest & reconsider. Until next time then.")
        return

    global enteredValues
    enteredValues = []
    global enteredData

    while iterationValue > count:
        print("")
        try:
            enteredValues.append(int(input("Please enter an integer value: ")))

            count += 1
            #goOn = str(input("Do you wish to continue? Enter 'Q' or 'q' to quit, otherwise enter any other character to continue: "))
            '''if enteredValues in range(0, count):
            enteredValues.append(count)
            print("The minimum or the least number in the list is: ", enteredValues[count])'''
        except:
            print("")
            print("Invalid value entered. ")

    print("")
    if str(iterationValue) != "0" and str(iterationValue).isnumeric() == True:
        print("This is the list of entered numbers: ", end="")
    else:
        print("We regret that you did not wish to play today. Please take a rest & reconsider. Until next time then.")
        return
    #if count >= 0 and count < 1000:


    for enteredData in range(0, count):
        print(enteredValues[enteredData], end=" ")
    print("")
    #count += 1
'''def getMinValue():
    if enteredValues[enteredData]: #< enteredValues[count]:
        print("")
        print("The minimum or least number in the list is: ", enteredValues[enteredData])
        print("")

def getMaxValue():
    if enteredValues[0]: #> enteredValues[count]:

        print("The maximum or largest number in the list is: ", enteredValues[enteredData])
        print("")'''

userInput()
#getMinValue()
#getMaxValue()
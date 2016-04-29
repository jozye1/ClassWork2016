# Python Assignment 3.3 - User Input
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier
# Date: 22 April 2016

def userInputMain():
    enteredValues = []
    iterationValue = 0
    print("")
    print("--THIS PROGRAM ALLOWS FOR ENTERING A LIST OF NUMBERS, THEN WILL SORT THE LIST AND SHOWS THE LOWEST & HIGHEST VALUE--")
    count = 0
    counter = 0
    goodData = True
    while goodData == True:
        #counter += 1
        try:
            print("")
            iterationValue = int(input("Please Enter The Number Of Times You Wish To Enter A Value: "))
            count += 1
            #goodData = False
            break
        except:
            print("")
            if counter >= 0:
                print("\tThis program only accepts numeric characters.")

            if count <= 0:
                counter = 2
                count = 1
                print("\tYou have",counter,"more chances to try again.")
            elif count <= 1:
                counter = 1
                count = 2
                print("\tYou have",counter,"more chance to try again.")
                count = 3
                counter = -1
            elif count == 3:
                print("We regret that you're not willing to play & enjoy the game at this moment. Please come back later.")
                print(
                    "----------------------------------------------------------------------------------------------------------")
                count = 0
                return

    if iterationValue <= 0:
        return
    #----

    count = 0
    counter = 0
    while iterationValue >= 0:
        #counter += 1
        try:
            print("")
            enteredValues.append(int(input("Please Enter A Number: ")))
            count += 1
            if iterationValue <= count:
                break
        except:
            print("")
            if counter >= 0:
                print("\tThis program only accepts numeric values.")

            if count <= 0:
                counter = 2
                count = 1
                print("\tYou have",counter,"more opportunities to try again.")
            elif count <= 1:
                counter = 1
                count = 2
                print("\tYou have",counter,"more opportunity to try again.")
                count = 3
                counter = -1
            elif count == 3:
                print("We regret that you're not willing to continue playing & enjoying the game at this moment. Please come back later.")
                print(
                    "----------------------------------------------------------------------------------------------------------")
                count = 0
                return

    if iterationValue <= 0:
        return
    #------

    print("")
    print("This is the list of entered numbers: ", end="")

    for enteredData in range(0, iterationValue):
        print(enteredValues[enteredData], end=" ")
    enteredValues.sort()
    print("")
    print("The numbers list sorted out: ",enteredValues)

    print("")

    print("The minimum or least number entered in the list is: ", enteredValues[0])
    print("The maximum or largest number entered in the list is: ", enteredValues[iterationValue -1])
    print("----------------------------------------------------------------------------------------------------------")

    if iterationValue < 0:
        return

userInputMain()
#------

def repeatingProcess():

    keepingGoing = True
    while keepingGoing == True:
        print("")
        goOn = str(input("|Do you wish to try again? Enter 'Q' or 'q' to quit, otherwise enter any other character to start over|: "))
        print("==========================================================================================================")
        print("")
        if goOn == str("Q") or goOn == str("q"):
            goodData = False
            keepingGoing = False
            return
        else:
            userInputMain()

repeatingProcess()

print("")
print("Thank you for taking part in our promotion! Please come back again soon! Have a great day!!!")
print("")






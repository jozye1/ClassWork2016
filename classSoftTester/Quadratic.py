# Python Assignment 3.2 - Quadratic Formula
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier

def quadratic():
    print("")
    print("This program will take integer values and will print out a Trinomial/Quadratic expression in the format of (AX²+BX+C), along with its calculated value. ")
    print("")

    goOn = True
    while goOn == True:
        try:
            valueA = int(input("Please enter a value for A: "))
            valueB = int(input("Please enter a value for B: "))
            valueC = int(input("Please enter a value for C: "))
            valueX = int(input("Please enter a value for X: "))

            print("The following expression is the quadratic formula for the values entered:  ", end="")
            print(valueA,"X^2+",valueB,"X+",valueC)

            quadraticFormula = float((valueA * valueX ** 2) + (valueB * valueX) + (valueC))

            print("The value of the quadratic expression is: ", quadraticFormula)
            print("")
        except:
            print("Please enter a valid integer: ", end="")
        noMore = str(input("Wish to test more values? Enter 'Y' or 'y' to proceed: "))
        if noMore == "Y" or noMore == "y":
            goOn = True
        else:
            goOn = False

    print("")
    print("I, Josue, thank you for your participation! Please come back again soon for more!")
    print("")

quadratic()
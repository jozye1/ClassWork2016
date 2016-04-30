# Python Programming Activity - Favorite Colors
# Instructor:  Eduardo Hernandez
# Course: Software Tester
# Author: Josue Merisier
# Date: 22 April 2016

def listings():
    print("")
    print("This program accepts names and favorite colors, then prints a list of names along with their favorite colors.")
    print("")
    nameList = getNamesAndColors()

def getNamesAndColors():
    names = []
    colors = []
    count = 0
    exit = False

    while exit == False:
        names.append(str(input("Please enter your name: ")))
        colors.append(str(input("Please enter your favorite color: ")))
        count +=1
        continuePlaying = str(input("Enter 'Q' or 'q' to quit. Any other character entered will continue the game: "))

        if continuePlaying == str("Q") or continuePlaying == str("q"):
            exit = True
        else:
            exit = False

    for info in range(0, count):
        print("")
        print(names[info], end="'s ")
        print("favorite color is: ", end="")
        print(colors[info])

listings()
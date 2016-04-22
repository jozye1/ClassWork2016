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

    if continuePlaying == "Q" or continuePlaying == "q":
        exit = True

    print(names[count], end=" ")
    print("favorite color is: ", end="")
    print(colors[count])

listings()
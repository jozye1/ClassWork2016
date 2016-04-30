def TodaysTemp():
    fahrenheit = 0
    celsius = float((fahrenheit - 32) / 1.8)
    fahrenheit = float((1.8 * celsius) + 32)

    continue_entry = True

    while continue_entry == True:

        try:
            print("")
            temperature = float(input("Please enter today's temperature in Fahrenheit: "))
            print("")
            celsius = round((temperature - 32) / 1.8, 2)
            print(temperature,end=" ")
            print("degree(s) Fahrenheit = " ,end="")
            print(celsius,end="")
            print(" degree(s) Celsius.")

        except:
            print("")
            print("Please enter a valid whole or decimal number. ")
        print("")
        proceed = str(input("Wish to continue? 'Y' or 'y', otherwise enter any other character to end the game: "))
        if proceed == "Y" or proceed== "y":
            continue_entry = True
        else:
            continue_entry = False

    print("")
    print("Thank you for your participation! Have a great day!!!")

TodaysTemp()
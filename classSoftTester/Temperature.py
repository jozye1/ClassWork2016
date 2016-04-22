def TodaysTemp():
    fahrenheit = 0
    celsius = float((fahrenheit - 32) / 1.8)
    fahrenheit = float((1.8 * celsius) + 32)

    continue_entry = True

    while continue_entry == True:
        temperature = float(input("Please enter today's temperature in Fahrenheit: "))
        celsius = (temperature - 32) / 1.8
        print(temperature,end=" ")
        print("degree(s) Fahrenheit = " ,end="")
        print(celsius,end="")
        print(" degree(s) Celsius.")
        proceed = str(input("Do you wish to continue, Y or N? "))
        if proceed == "Y" or proceed== "y":
            continue_entry = True
        else:
            continue_entry = False

    print("")
    print("Thank you for your participation! Have a great day!!!")

TodaysTemp()
def weatherIncrement():

    print("")
    print("This program prints Celsius temperatures from 0-100, in increment of 5, along with the equivalents in Fahrenheit: ")
    print("")

    temp = 0
    for t in range(0,101,5):
        weatherTempf = (1.8 * temp) + 32
        print(temp, " Celsius is: " "\t", round(weatherTempf, 2), " Fahrenheit")
        temp += 5

weatherIncrement()
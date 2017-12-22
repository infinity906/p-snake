import datetime
import random
import mathematics as m
import countries as c
import weather as w

def main():
    print("Welcome to Inifinity Assistance System\n")

    print("Inifnity is a personal assistance system which can perform following task:\n"
          "1. Can be used as a calculator for compound calculations\n"
          "2. Can be used for knowing the weather condition of your region\n"
          "3. Can be used for knowing various statistics of various countries\n")

    option = input("Kindly select the required service from the below mentioned list\n"
                   "Mathematics = Mathematical Calculator\n"
                   "Weather = Get the updated weather conditions\n"
                   "Statistics = Get the updated statistics on any country of your choice\n"
                   "Exit = To exit from Inifinity Assistance System\n")

    return mode(option)


def mode(option):

    if option.lower() == "mathematics":
        print("Welcome to Mathematics module of infinity\n"
              "this module can assist you in various mathematical functions like addition, subtraction, multiplication and many more on any number that you provide\n"
              "Kindly follow the below mentioned instructions for the required result\n")
        m.mathematics()
    elif option.lower() == "weather":
        print("Welcome to weather module of infinity\n"
              "This module can assist you in informing about the current as well as the predict the future weather conditions\n"
              "Kindly follow the below mentioned instructions for the accurate weather conditions\n")
        w.weather()
    elif option.lower() == "statistics":
        print("Welcome to Statistics module of Inifinity\n"
              "This module can provide you various information like Population, location, Capital City, Currency, Area, etc of all the countries in the globe\n"
              "Kindly follow the below instructions for getting the precise information.\n")
        c.countries()
    elif option.lower() == "exit":
        print("Thank you for using Inifinity Assistance System")
    else:
        print("Sorry, This is not a valid input")

def retrying (mode1):
    retry = input('''
                    Do you want to use this module again ?
                    Y or N. \n''')

    if retry.upper() == 'Y':
        function = globals()[mode1]
        function()
    else:
        print("Thankyou for using ", mode1, "module in Inifinity")
        return main()


if __name__=="__main__":
    main()

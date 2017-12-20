import datetime
import random
def main():
    print("Welcome to Inifinity Assistance System\n")

    print("Inifnity is a personal assistance system which can perform following task:\n"
          "1. Can be used as a calculator for compound calculations\n"
          "2. Can be used for knowing the weather condition of your region\n"
          "3. Can be used for knowing various statistics of various countries\n")

    option = input("Kindly select the required service from the below mentioned list\n"
                   "Math = Mathematical Calculator\n"
                   "Weather = Get the updated weather conditions\n"
                   "Statistics = Get the updated statistics on any country of your choice\n"
                   "Exit = To exit from Inifinity Assistance System\n")

    return mode(option)


def mode(option):

    if option.lower() == "mathematics":
        num1 = input('Please enter the first number\n')
        num2 = input("Please enter the second number\n")
        mathematics(num1, num2)
    elif option.lower() == "weather":
        weather()
    elif option.lower() == "statistics":
        countries()
    elif option.lower() == "exit":
        print("Thank you for using Inifinity Assistance System")
    else:
        print("Sorry, This is not a valid input")


def validateNumber(number):
    print("Welcome to Mathematics module of infinity\n"
          "this module can assist you in various mathematical functions like addition, subtraction, multiplication and many more on any number that you provide\n"
          "Kindly follow the below mentioned instructions for the required result\n")
    try:
        value = float(number)
        return True
    except ValueError:
        return False


def mathematics(num1, num2):
    if validateNumber(num1):
        num1 = float(num1)
        if validateNumber(num2):
            num2 = float(num2)

            operation = input('''
                        Please type in the math operation you would like to complete:
                        + for addition
                        - for subtraction
                        * for multiplication
                        / for division
                        % for modulus
                        ^ for exponent
                        ''')

            if operation == '+':
                print(num1, "+", num2, "=", num1 + num2)

            elif operation == '-':
                print(num1, "-", num2, "=", num1 - num2)

            elif operation == '*':
                print(num1, "*", num2, "=", num1 * num2)

            elif operation == '/':
                print(num1, "/", num2, "=", num1 / num2)

            elif operation == '%':
                print(num1, "%", num2, "=", num1 % num2)

            elif operation == '^':
                print(num1, "^", num2, "=", num1 ** num2)

            else:
                print("You have not typed a valid operator, please run the program again.")
                calculator()
        else:
            print("You have entered an invalid character2. Please enter any numerical value for the calculation")
            calculator()
    else:
        print("You have entered an invalid character1. Please enter any numerical value for the calculation")
        calculator()

    return retrying("mathematics")




list_of_countries = {
        1 : {
            'name': 'Canada',
            'location': 'North America',
            'capital city': 'Ottawa',
            'currency':'Canadian Dollar',
            'population':'32,268,240',
            'area':'9,970,610 square km'
        },
        2: {
            'name': 'India',
            'location': 'Asia',
            'capital city': 'New Delhi',
            'currency': 'Indian Rupee',
            'population': '1,103,371,000',
            'area': '3,287,263 square km'
        },
        3:{
            'name': 'Albania',
            'location': 'Europe',
            'capital city': 'Tirana',
            'currency': 'Albania Lek',
            'population': '3,129,678',
            'area': '28,748 square km'
        },
        4:{
            'name': 'Ireland',
            'location': 'Europe',
            'capital city': 'Dublin',
            'currency': 'Euro',
            'population': '4,147,901',
            'area': '70,273 square km'
        },
        5:{
            'name': 'Singapore',
            'location': 'Asia',
            'capital city': 'Singapore',
            'currency': 'Brunei dollar; Singapore Dollar',
            'population': '4,483,900',
            'area': '699 square km'
        },
        6:{
            'name': 'Germany',
            'location': 'Europe',
            'capital city': 'Berlin',
            'currency': 'Euro',
            'population': '82,689,210',
            'area': '357,022 square km'
        }
    }

def countries():
    print("Welcome to Statistics module of Inifinity\n"
          "This module can provide you various information like Population, location, Capital City, Currency, Area, etc of all the countries in the globe\n"
          "Kindly follow the below instructions for getting the precise information.\n")
    global list_of_countries
    search = input('Please enter your query\n')
    search1 = search.split()
    if search.lower() == 'population':
        for i in range (1,7):
            print("The population of", list_of_countries[i]['name'], "is", list_of_countries[i]['population'])

    elif search.lower() == 'location':
        for i in range (1,7):
            print("The location of", list_of_countries[i]['name'], "is", list_of_countries[i]['location'])

    elif search.lower() == 'capital city':
        for i in range (1,7):
            print("The capital city of", list_of_countries[i]['name'], "is", list_of_countries[i]['capital city'])

    elif search.lower() == 'currency':
        for i in range (1,7):
            print("The currency of", list_of_countries[i]['name'], "is", list_of_countries[i]['currency'])

    elif search.lower() == 'area':
        for i in range (1,7):
            print("The area of", list_of_countries[i]['name'], "is", list_of_countries[i]['area'])

    else:
        try:
            country = search1[2]
            specific = search1[0]

            for i in range (1,7):
                if country.lower() == list_of_countries[i]['name'].lower():
                    print(specific, "of", country, "is", list_of_countries[i][specific] )
                    countries()
                elif (country.lower() != list_of_countries[i]['name'].lower()) and (i == 6) :
                    print("Sorry, the information is not present in the database.")
                    countries()
        except IndexError:
            print("Please enter a valid query.")
            countries()
        except KeyError:
            print("Sorry, the information is not present in the database.")
            countries()

        return retrying("statistics")


def weatherlib(date):
    if date.lower() == 'january':
        num = list(range(-12, 10))
        temp = random.choice(num)
        # January = print("-4.6 degree celcius")
    elif date.lower() == 'february':
        num = list(range(-11, -9))
        temp = random.choice(num)
        # february = print("-4.0 degree celcius")
    elif date.lower() == 'march':
        num = list(range(8, 13))
        temp = random.choice(num)
        # March = print("10 degree celcius")
    elif date.lower() == 'april':
        num = list(range(9, 16))
        temp = random.choice(num)
        # April = print("12 degree celcius")
    elif date.lower() == 'may':
        num = list(range(11, 18))
        temp = random.choice(num)
        # May = print("20 degree celcius")
    elif date.lower() == 'june':
        num = list(range(10, 17))
        temp = random.choice(num)
        # June = print("22 degree celcius")
    elif date.lower() == 'july':
        num = list(range(20, 28))
        temp = random.choice(num)
        # July = print("33 degree celcius")
    elif date.lower() == 'august':
        num = list(range(21, 25))
        temp = random.choice(num)
        # August = print("38 degree celcius")
    elif date.lower() == 'september':
        num = list(range(5, 10))
        temp = random.choice(num)
        # Spetember = print("18 degree celcius")
    elif date.lower() == 'october':
        num = list(range(5, 8))
        temp = random.choice(num)
        # October = print("13 degree celcius")
    elif date.lower() == 'november':
        num = list(range(-8, -5))
        temp = random.choice(num)
        # Novenber = print("4 degree celcius")
    elif date.lower() == 'december':
        num = list(range(-10, -6))
        temp = random.choice(num)
        # December = print("-3 degree celcius")

    return temp


def weather ():
    now = datetime.datetime.now()
    print("Welcome to weather module of infinity\n"
          "This module can assist you in informing about the current as well as the predict the future weather conditions\n"
          "Kindly follow the below mentioned instructions for the accurate weather conditions\n")

    query = input("Enter your query\n")

    if query.lower() == 'what is the weather':

        # print (now.strftime("%B"))
        date = (now.strftime("%B"))
        temp = weatherlib(date)
        print("Weather in toronto now is ", temp, "Degree Celsius,", temp * 1.8 + 32, "Degree Fahrenheit")
    else:
        qlist = query.split()
        date = qlist[5]
        temp = weatherlib(date)
        print("Weather in toronto in", date," is ", temp, "Degree Celsius,", temp * 1.8 + 32, "Degree Fahrenheit")

def retrying (mode1):
    retry = input('''
                    Do you want to use this module again ?
                    Y or N. ''')

    if retry.upper() == 'Y':
        mode(option=mode1)
    else:
        print("Thankyou for using ", mode1, "module in Inifinity")
        return main()


if __name__=="__main__":
    main()
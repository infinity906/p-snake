import random
import datetime

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
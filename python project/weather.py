import random
import datetime
import infinity123 as i

def weatherlib(date):
    if date.lower() == 'january':
        num = list(range(-12, 10))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # January = print("-4.6 degree celcius")
    elif date.lower() == 'february':
        num = list(range(-11, -9))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # february = print("-4.0 degree celcius")
    elif date.lower() == 'march':
        num = list(range(8, 13))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # March = print("10 degree celcius")
    elif date.lower() == 'april':
        num = list(range(9, 16))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # April = print("12 degree celcius")
    elif date.lower() == 'may':
        num = list(range(11, 18))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # May = print("20 degree celcius")
    elif date.lower() == 'june':
        num = list(range(10, 17))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # June = print("22 degree celcius")
    elif date.lower() == 'july':
        num = list(range(20, 28))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # July = print("33 degree celcius")
    elif date.lower() == 'august':
        num = list(range(21, 25))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # August = print("38 degree celcius")
    elif date.lower() == 'september':
        num = list(range(5, 10))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # Spetember = print("18 degree celcius")
    elif date.lower() == 'october':
        num = list(range(5, 8))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # October = print("13 degree celcius")
    elif date.lower() == 'november':
        num = list(range(-8, -5))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # Novenber = print("4 degree celcius")
    elif date.lower() == 'december':
        num = list(range(-10, -6))
        temp = random.choice(num)
        temp1 = temp * 1.8 + 32
        # December = print("-3 degree celcius")
    else:
        temp = 0
        temp1 = 0
        print ("Please enter a valid query")
    return temp, temp1


def weather ():
    now = datetime.datetime.now()
    query = input("Enter your query\n")
    try:
        if query.lower() == 'what is the weather':
            # print (now.strftime("%B"))
            date = (now.strftime("%B"))
            temp, temp1 = weatherlib(date)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp1, "Degree Fahrenheit")
        else:
            qlist = query.split()
            date = qlist[5]
            temp, temp1 = weatherlib(date)
            if temp != 0 and temp1 != 0:
                print("Weather in toronto in", date," is ", temp, "Degree Celsius,", temp1, "Degree Fahrenheit")
    except Exception:
        print("Please enter a valid query.")
        weather()
    except KeyError:
        print("Sorry, the information is not present in the database.")
        weather()

    retry = input('''
                    Do you want to use this module again ?
                    Y or N. \n''')

    if retry.upper() == 'Y':
        weather()
    else:
        print("Thankyou for using mathematics module in Inifinity")
        return i.main()

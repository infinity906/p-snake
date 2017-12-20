def weather ():
    import random
    import datetime
    now = datetime.datetime.now()

    print("Welcome")

    query = input("Enter your query\n")

    if query.lower() == 'what is the weather':
        #print (now.strftime("%B"))
        date = (now.strftime("%B"))

        if date == 'January':
            num = list(range(-12, 10))
            temp = random.choice(num)
            print("Weather in toronto now is ",temp, "Degree Celsius,",temp + 32, "Degree Fahrenheit" )
            #January = print("-4.6 degree celcius")
        elif date == 'February':
            num = list(range(-11, -9))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #february = print("-4.0 degree celcius")
        elif date == 'March':
            num = list(range(8, 13))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #March = print("10 degree celcius")
        elif date == 'April':
            num = list(range(9, 16))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #April = print("12 degree celcius")
        elif date == 'May':
            num = list(range(11, 18))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #May = print("20 degree celcius")
        elif date == 'June':
            num = list(range(10, 17))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #June = print("22 degree celcius")
        elif date == 'July':
            num = list(range(20, 28))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #July = print("33 degree celcius")
        elif date == 'August':
            num = list(range(21, 25))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #August = print("38 degree celcius")
        elif date == 'September':
            num = list(range(5, 10))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #Spetember = print("18 degree celcius")
        elif date == 'October':
            num = list(range(5, 8))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #October = print("13 degree celcius")
        elif date == 'November':
            num = list(range(-8, -5))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #Novenber = print("4 degree celcius")
        elif date == 'December':
            num = list(range(-10, -6))
            temp = random.choice(num)
            print("Weather in toronto now is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            #December = print("-3 degree celcius")

    else:
        qlist = query.split()
        month = qlist[5]
        query1 = month.lower()
        if query1 == 'january':
            num = list(range(-12, 10))
            temp = random.choice(num)
            print("Weather in toronto in January is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # January = print("-4.6 degree celcius")
        elif query1 == 'february':
            num = list(range(-11, -9))
            temp = random.choice(num)
            print("Weather in toronto in February is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # february = print("-4.0 degree celcius")
        elif query1 == 'march':
            num = list(range(8, 13))
            temp = random.choice(num)
            print("Weather in toronto in March is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # March = print("10 degree celcius")
        elif query1 == 'april':
            num = list(range(9, 16))
            temp = random.choice(num)
            print("Weather in toronto in April is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # April = print("12 degree celcius")
        elif query1 == 'may':
            num = list(range(11, 18))
            temp = random.choice(num)
            print("Weather in toronto in May is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # May = print("20 degree celcius")
        elif query1 == 'june':
            num = list(range(10, 17))
            temp = random.choice(num)
            print("Weather in toronto in June is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # June = print("22 degree celcius")
        elif query1 == 'july':
            num = list(range(20, 28))
            temp = random.choice(num)
            print("Weather in toronto in July is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # July = print("33 degree celcius")
        elif query1 == 'august':
            num = list(range(21, 25))
            temp = random.choice(num)
            print("Weather in toronto in August is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # August = print("38 degree celcius")
        elif query1 == 'september':
            num = list(range(5, 10))
            temp = random.choice(num)
            print("Weather in toronto in September is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # Spetember = print("18 degree celcius")
        elif query1 == 'october':
            num = list(range(5, 8))
            temp = random.choice(num)
            print("Weather in toronto in October is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # October = print("13 degree celcius")
        elif query1 == 'november':
            num = list(range(-8, -5))
            temp = random.choice(num)
            print("Weather in toronto in November is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # Novenber = print("4 degree celcius")
        elif query1 == 'december':
            num = list(range(-10, -6))
            temp = random.choice(num)
            print("Weather in toronto in December is ", temp, "Degree Celsius,", temp + 32, "Degree Fahrenheit")
            # December = print("-3 degree celcius")

    retry = input('''
Do you want to see weather prediction again ?
Y or N. 
''')

    if retry.upper() == 'Y':
        weather()
        # else
        #   main()

weather ()


import infinity as i

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

    retry = input('''
                    Do you want to use the statistics module again ?
                    Y or N. ''')

    if retry.upper() == 'Y':
        i.mode(option="statistics")
    else:
        return "Thank you for using statistics module in Inifinity", i.main()
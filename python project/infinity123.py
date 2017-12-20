

print("Welcome to Inifinity Assistance System\n")

print("Inifnity is a personal assistance system which can perform following task:\n"
      "1. Can be used as a calculator for compound calculations\n"
      "2. Can be used for knowing the weather condition of your region\n"
      "3. Can be used for knowing various statistics of various countries\n")



def mode(option):
    import calculator1 as m
    import weather as w
    import countries as c

    if option.lower() == "math":
        num1 = input('Please enter the first number\n')
        num2 = input("Please enter the second number\n")
        m.mathematics(num1, num2)
    elif option.lower() == "weather":
        w.weather()
    elif option.lower() == "statistics":
        c.countries()
    elif option.lower() == "exit":
        print("Thank you for using Inifinity Assistance System")
    else:
        print("Sorry, This is not a valid input")

def main():
    option = input("Kindly select the required service from the below mentioned list\n"
                   "Math = Mathematical Calculator\n"
                   "Weather = Get the updated weather conditions\n"
                   "Statistics = Get the updated statistics on any country of your choice\n"
                   "Exit = To exit from Inifinity Assistance System\n")

    return mode(option)

if __name__=="__main__":
    main()
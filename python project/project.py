import datetime
import random
def calculator():
    b1=input("enter first number")
    if b1 == type(int) or b1 == type(float):
        b2 = input("enter second number")
        if b2 == type(int) or b2 == type(float):
            b3 = input("what would you like to calculate \n"
                       "Press + for addition \n"
                       "Press - for subtraction \n"
                       "Press / for division \n"
                       "Press * for multiplication \n"
                       "Press % for remainder \n")
            if b3 == "+":
                result = b1 + b2
            elif b3 == "-":
                result = b1 - b2
            elif b3 == "/":
                result = b1 / b2
            elif b3 == "*":
                result = b1 * b2
            elif b3 == "%":
                result = b1 % b2
            else:
                print("not valid input")
            return result



        else:
            print("enter valid input")
    else:
        print("enter valid input")

def main():
    a=input("Hello! This is RAVI. What would You like to know Today! \n"
            "Press 1 for calculator \n"
            "Press 2 to know weather of countries \n"
            "Press 3 for statistics of countries \n"
            "ENJOY!")
    if a == "1" :
        result1 = calculator()
        print("Result of your calculatin is", result1)
    elif a == "2":
     weather()

    elif a == "3":
        stat()
    else:
        print("Pleas enter valid input! \n"
              "THANK YOU!")




def weather():
    current = datetime.datetime.now()
    w = input("Enter Quary \n"
              "press 1 for current weather in Toronto \n"
              "Press 2 to check weather in any month")
    if w == "1":
        month = (current.strftime("%B"))
        print(month)
    elif w == "2":
        month = str(input("enter month"))
    else:
        print("input not valid")
    #klsjdlajsd\
    if month.lower() == 'january':
        abc(l=-12, u=10)
    elif month.lower() == 'feb':
        abc(l=-11, u=-9)
    elif month.lower() == 'march':
            abc(l=8, u=13)
    elif month.lower() == 'april':
            abc(l=9, u=16)
    elif month.lower() == 'may':
            abc(l=11, u=18)
    elif month.lower() == 'june':
            abc(l=10, u=17)
    elif month.lower() == 'july':
            abc(l=20, u=28)
    elif month.lower() == 'aug':
            abc(l=21, u=25)
    elif month.lower() == 'sept':
            abc(l=5, u=10)
    elif month.lower() == 'oct':
            abc(l=5, u=9)
    elif month.lower() == 'nov':
            abc(l=-6, u=2)
    elif month.lower() == 'december':
            abc(l=-11, u=0)
    else:
            print("enter valid month")
    print("weather of toronto in", month, "is", temp, "degree celsius", temp * 1.8 + 32, "degree Fahrenheit")

            #monthTup=tuple("jan", "Feb","march","april","may","june","july","aug","sept", "oct", "nov","dec")


def abc(l,u):
    global temp
    num=list(range(l,u))
    temp=random.choice(num)
    return temp
    #print("weather of toronto in", month, "is", temp, "degree celsius", temp * 1.8 + 32, "degree Fahrenheit")



def stat():
    print("n")


if __name__ =="__main__" :
    main()
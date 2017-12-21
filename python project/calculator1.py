from msvcrt import getch

def validateNumber(number):
    try:
        value = float(number)
        return True
    except ValueError:
        return False



def mathematics(num1):
    print("Welcome to Mathematics module of infinity\n"
          "this module can assist you in various mathematical functions like addition, subtraction, multiplication and many more on any number that you provide\n"
          "Kindly follow the below mentioned instructions for the required result\n")
    if validateNumber(num1):

        num1 = float(num1)

        while True:
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
                num2 = input("Please enter the second number\n")
                if validateNumber(num2):
                    num2 = float(num2)
                else:
                    print("You have entered an invalid character2. Please enter any numerical value for the calculation")
                    mathematics()
                result = num1 + num2

            elif operation == '-':
                num2 = input("Please enter the second number\n")
                if validateNumber(num2):
                    num2 = float(num2)
                else:
                    print("You have entered an invalid character2. Please enter any numerical value for the calculation")
                    mathematics()
                result = num1 - num2

            elif operation == '*':
                num2 = input("Please enter the second number\n")
                if validateNumber(num2):
                    num2 = float(num2)
                else:
                    print("You have entered an invalid character2. Please enter any numerical value for the calculation")
                    mathematics()
                result = num1 * num2

            elif operation == '/':
                num2 = input("Please enter the second number\n")
                if validateNumber(num2):
                    num2 = float(num2)
                else:
                    print("You have entered an invalid character2. Please enter any numerical value for the calculation")
                    mathematics()
                result = num1 / num2

            elif operation == '%':
                num2 = input("Please enter the second number\n")
                if validateNumber(num2):
                    num2 = float(num2)
                else:
                    print("You have entered an invalid character2. Please enter any numerical value for the calculation")
                    mathematics()
                result = num1 % num2

            elif operation == '^':
                num2 = input("Please enter the second number\n")
                if validateNumber(num2):
                    num2 = float(num2)
                else:
                    print("You have entered an invalid character2. Please enter any numerical value for the calculation")
                    mathematics()
                result = num1 ^ num2

            else:
                print("You have not typed a valid operator, please run the program again.")
                mathematics()
            print (result)
            answer = input("Continue calculation ? y/n")
            if answer.lower() == "n" or answer.lower()=="no":
                break
            else :
                num1 = result
                print (num1)

    else:
        print("You have entered an invalid character1. Please enter any numerical value for the calculation")
        mathematics()

import infinity as i

def validateNumber(number):
    print("Welcome to Mathematics module of infinity\n"
          "this module can assist you in various mathematical functions like addition, subtraction, multiplication and many more on any number that you provide\n"
          "Kindly follow the below mentioned instructions for the required result\n")
    try:
        value = float(number)
        return True
    except ValueError:
        return False

    

def mathematics(num1,num2):
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

    retry = input('''
                Do you want to use Mathematics module again ?
                Y or N. ''')

    if retry.upper() == 'Y':
        i.mode(option="math")
    else:
        return "Thank you for using Mathematics module in Inifinity", i.main()






print("Welcome")

def validateNumber(number):
    try:
        value = float(number)
        return True
    except ValueError:
        return False

    

def calculator():
    num1 = input('Please enter the first number\n')
    if validateNumber(num1): 
        num1=float(num1)
        num2 = input("Please enter the second number\n")
        if validateNumber(num2):
            num2=float(num2)

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
        Do you want to calculate again ?
        Y or N. ''')

    if retry.upper() == 'Y':
        calculator()
        # else
        #   main()
calculator()



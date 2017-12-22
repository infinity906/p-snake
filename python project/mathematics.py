import infinity123 as i

def validateNumber(number):
    try:
        value = float(number)
        return True
    except ValueError:
        return False



def mathematics():
    num1 = input('Please enter the first number\n')
    if validateNumber(num1):
#to check if the number is float
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
                continue
            print (result)
            answer = input("Continue calculation ? y/n\n")
            if answer.lower() == "n" or answer.lower()=="no":
                break
            else :
                num1 = result
                print (num1)

    else:
        print("You have entered an invalid character1. Please enter any numerical value for the calculation")
        mathematics()

    retry = input('''
                    Do you want to use this module again ?
                    Y or N. \n''')

    if retry.upper() == 'Y':
        mathematics()
    else:
        print("Thankyou for using mathematics module in Inifinity")
        return i.main()

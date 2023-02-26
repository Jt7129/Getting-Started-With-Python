def clac():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    operator = input("Choose a Operator\n+\n-\n*\n/\nEnter you operator: ")

    if operator == "+":
        addvar = num1 + num2
        print("You got,", addvar)
    elif operator == "-":
        subvar = num1 - num2
        print("You got,", subvar)
    elif operator == "*":
        mulvar = num1 * num2
        print("You got,", mulvar)
    elif operator == "/":
        divar = num1 / num2
        print("You got,", divar)
    else:
        clac()

clac()

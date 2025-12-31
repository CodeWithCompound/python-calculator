def calculator():
    try:
        num1 = float(input("first number: "))
        operator = input("operator (+, -, *, /): ")
        num2 = float(input("second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("ERR: my math teacher would scream: can't divide by zero")
                return
            result = num1 / num2
        else:
            print("ERR: operator must be +, -, *, /")
            return

        print(f"Result: {result}")
        playAgain = input("Another question? y/n: ")
        if playAgain == 'y':
            calculator()

    except ValueError:
        print("ERR: enter valid number (no letters)")


calculator()

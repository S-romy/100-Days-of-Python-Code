from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}


def calculator():
    print(logo)

    first_number = float(input("What's the first number?: "))

    re_run = True

    while re_run:
        for symbol in operations:
            print(symbol)

        symbol = input("Pick an operator: ")

        second_number = float(input("What's the next number?: "))

        answer = operations[symbol](first_number, second_number)

        print(f"{first_number} {symbol} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ")
        if choice == 'y':
            first_number = answer
        else:
            re_run = False
            print("\n" * 20)

            calculator()


calculator()

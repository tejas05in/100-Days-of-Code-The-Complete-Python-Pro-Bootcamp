from art import logo
import os


def add(num1, num2):
    """function to add 2 numbers in the calculator app

    Args:
        num1 (int): integer
        num2 (int): integer

    Returns:
        int: num1 + num2
    """
    return num1 + num2


def subtract(num1, num2):
    """function to subtract 2 numbers in the calculator app

    Args:
        num1 (int): integer
        num2 (int): integer

    Returns:
        int: num1 - num2
    """
    return num1 - num2


def multiply(num1, num2):
    """function to multiply 2 numbers in the calculator app

    Args:
        num1 (int): integer
        num2 (int): integer

    Returns:
        int: num1 * num2
    """
    return num1 * num2


def divide(num1, num2):
    """function to divide 2 numbers in the calculator app

    Args:
        num1 (int): integer
        num2 (int): integer

    Returns:
        int: num1 / num2
    """
    return num1 / num2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))

    for i in operations:
        print(i)

    proceed = True
    while proceed:
        operator = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        function = operations[operator]
        result = function(num1, num2)
        print(
            f"{num1} {operator} {num2} = {function(num1, num2)}")
        decision = input(
            f"Type 'y' to continue calculating with {result}, or 'q' tp quit, or type 'n' to start a new calculation: ")
        if decision == "y":
            num1 = result
        elif decision == "n":
            return calculator()
        else:
            proceed = False


calculator()

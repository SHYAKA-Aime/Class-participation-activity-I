#!/usr/bin/env python3

def calculator(num1, num2, operation):
    """
    Performs a basic arithmetic operation on two numbers.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Invalid operation."

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter an operation (+, -, *, /): ")

num1 = float(num1)
num2 = float(num2)

result = calculator(num1, num2, operation)
print("Result:", result)

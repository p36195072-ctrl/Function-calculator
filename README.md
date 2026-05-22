Function Calculator

A beginner-friendly Python project that demonstrates how to use functions to perform basic calculator operations.

📌 Description

This program:

Creates separate functions for:
Addition
Subtraction
Multiplication
Division
Takes two numbers as input from the user
Performs all mathematical operations
Handles invalid input and division by zero errors using try-except

 Concepts Used

Functions
return statement
User Input
Integer Conversion using int()
Arithmetic Operators
try-except
ValueError
ZeroDivisionError

💻 Code

try:
    def add(a, b):
        return (a + b)

    def sub(a, b):
        return (a - b)

    def multi(a, b):
        return (a * b)

    def divi(a, b):
        return (a / b)

    num1 = int(input("enter your number:"))
    num2 = int(input("enter your number:"))

    print("addition = ", add(num1, num2))
    print("subtraction = ", sub(num1, num2))
    print("division = ", divi(num1, num2))
    print("multiplication = ", multi(num1, num2))

except ZeroDivisionError:
    print("can't be divided by 0")

except ValueError:
    print("Please enter valid numbers")

▶️ Example Output

enter your number: 10
enter your number: 5

addition = 15
subtraction = 5
division = 2.0
multiplication = 50
enter your number: 10
enter your number: 0

can't be divided by 0

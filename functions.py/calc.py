def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def power(x, y):
    return x ** y
def square_root(x):
    return x ** 0.5
def logarithm(x, base):
    import math
    return math.log(x, base)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Factorial of first number:", factorial(num1))
print("Power:", power(num1, num2))
print("Square root of first number:", square_root(num1))
print("Logarithm of first number with base second number:", logarithm(num1, num2))
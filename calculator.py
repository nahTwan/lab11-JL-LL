"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/nahTwan/lab11-JL-LL
# Partner 1: Jordon Lawson
# Partner 2: Lucas Leinweber
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
     return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0

def logarithm(a, b):
    if b <= 0 or b == 1:
        raise ValueError("Invalid Base")
    if a <= 0:
        raise ValueError("Invalid A")
    return math.log(a,b)

def exponent(a, b):
    return a * b


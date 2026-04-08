"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
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
    try:
        return math.log(a,b)
    except ValueError:
        return 0

def exponent(a, b):
    return a * b


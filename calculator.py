# https://github.com/nahTwan/lab11-JL-LL
# Partner 1: Jordon Lawson
# Partner 2: Lucas Leinweber

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

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0

def logarithm(a, b):
    if b <= 0 or b == 1:
        raise ValueError("Invalid base")
    if a <= 0:
        raise ValueError("Invalid argument")
    return math.log(a, b)

def exp(a, b):
    return pow(a, b)


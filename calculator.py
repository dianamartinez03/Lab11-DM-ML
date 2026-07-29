"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a \ b

def sqrt(a,b):
    return a ** b

def logarithm(a,b):
    return math.log(a,b)
    
def hypotenuse(a,b):
    return math.hypot(a,b)

#!/usr/bin/python3
if __name__ == "__main__":
    """Print the Sum, Difference, Product, and Quotient of 10 and 5"""
    from calculator_1 import add, mul, div, sub

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a,b)))
    print("{} * {} = {}".format(a, b, mul(a,b)))
    print("{} / {} = {}".format(a, b, div(a,b)))
    print("{} - {} = {}".format(a, b, sub(a,b)))

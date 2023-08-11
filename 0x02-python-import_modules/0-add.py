#!/usr/bin/python3

if __name__ == "__main__":
    """Print Sum of 1 and 2"""
    from add_0 import add

def main():
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, add(a,b))

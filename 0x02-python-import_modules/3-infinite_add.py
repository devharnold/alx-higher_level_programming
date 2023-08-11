#!/usr/bin/python3

def calculate_total(args):
    """Calculate the sum of arguments"""
    return sum(int(arg) for arg in args)

if __name__ == "__main__":
    import sys
    
    arguments = sys.argv[1:]
    total = calculate_total(arguments)
    print(total)

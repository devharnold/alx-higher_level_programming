#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions.
"""

import sys

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n_str = sys.argv[1]

    if not is_integer(n_str):
        print("N must be a number")
        sys.exit(1)

    n = int(n_str)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    a = [[i, None] for i in range(n)]

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        return any(y == a[x][1] for x in range(n))

    def clear_a(x):
        """clear the answers from the point of failure on"""
        for i in range(x, n):
            a[i][1] = None

    def reject(x, y):
        """determine whether or not to reject the solution"""
        if already_exists(y):
            return False
        for i in range(x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
        return True

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if x == n - 1: 
                    print(a)
                else:
                    nqueens(x + 1)  


    nqueens(0)

if __name__ == "__main__":
    main()

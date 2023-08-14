#!/usr/bin/python3

# Check lengths of tuples (tuple_a, tuple_b)
def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)

    if lenA < 1:
        tuple_a = (0,0)
    elif lenB < 2:
        tuple_a = (tuple_a[0], 0)

    if lenB < 1:
        tuple_b = (0,0)
    elif lenB < 2:
        tuple_b = (tuple_b[0], 0)

    result_tuple = add_tuple(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return(result_tuple)

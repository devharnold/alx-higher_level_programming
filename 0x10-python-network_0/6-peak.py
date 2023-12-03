#!/usr/bin/python3

"""Description of the find peak"""
def find_peak(list_of_integers):
    length = len(list_of_integers)
    m = length // 2
    li = list_of_integers

    if m - 1 < 0 and m + 1 >= length:
        return li[m]
    elif m - 1 < 0:
        return li[m] if li[m] > li[m + 1] else li[m + 1]
    elif m + 1 >= length:
        return li[m] if li[m] > li[m - 1] else li[m - 1]

    if li[m - 1] < li[m] > li[m + 1]:
        return li[m]

    if li[m + 1] > li[m - 1]:
        return find_peak(li[m:])
    return find_peak(li[:m])



#!/usr/bin/python3
def fizzbuzz():
	for i in range(1, 101):
		if i % 3 == 0:
			print("Fizz", end="")
		elif i % 5 == 0:
			print("Buzz", end="")
		elif i % 3 != 0 and 1 % 5 != 0:
			print('{:d}'.format(i), end="")
		else:
			print(i, end=' ')

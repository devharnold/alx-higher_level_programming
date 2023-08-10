#!/usr/bin/python3
def remove_char_cat(string, n):
     if n >= 0:
	return string[:n] + string[n + 1:]
     else:
	return string

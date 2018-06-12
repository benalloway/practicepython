# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

# [ expression for item in list if conditional ]

# First Attempt:

import random

# generate random list of random numbers with random length between 5 and 30 items long.
a = [random.randint(1,100) for x in range(0, random.randint(5,30))]

# function that returns list of two items: first and last item in given list.
def bookEnd(i):
	return [i[0], i[-1]]

# print list, and print first/last item
print(a)
print(bookEnd(a))
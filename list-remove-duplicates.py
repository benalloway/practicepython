# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:
# 1) Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# 2) Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def list():
	import random
	l = []
	for x in range(random.randint(5,50)):
		 l.append(random.randint(1,100))
	return l

def uniqueList(lst):
	newlst = []
	for x in lst:
		if x not in newlst:
			newlst.append(x)
	return newlst

print(uniqueList(list()))
# Take a list, say for example this one, 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


# first attempt, going for the basics:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for x in a:
# 	if x < 5:
# 		print(x)

# second attempt, extras 1:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# n = []
# for x in a:
# 	if x < 5:
# 		n.append(x)
# print(n)

# third attemp, extras 2:
print([x for x in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if x < 5])
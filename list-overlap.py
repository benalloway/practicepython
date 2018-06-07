# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:
# 1) Randomly generate two lists to test this
# 2) Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


# First attempt.

# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# def commonality(a, b):
# 	length = ''
# 	result = []

# 	if a > b or a == b:
# 		length = len(a)
# 		for i in range(length):
# 			if a[i] in b:
# 				result.append(a[i])
# 	else:
# 		length = len(b)
# 		for i in range(length):
# 			if b[i] in a:
# 				result.append(b[i])

# 	return set(result)
# print(commonality(a, b))

# Second attempt.
# import random
# list_lengths = random.sample(range(1,30), 2)
# list0 = random.sample(range(1,100), list_lengths[0])
# list1 = random.sample(range(1,100), list_lengths[1])

# def common(a,b):
# 	length = ''
# 	result = []

# 	if a > b or a == b:
# 		length = len(a)
# 		for i in range(length):
# 			if a[i] in b:
# 				result.append(a[i])
# 	else:
# 		length = len(b)
# 		for i in range(length):
# 			if b[i] in a:
# 				result.append(b[i])

# 	print(result)
# common(list0, list1)

# Third attempt: shorten code.
import random
list_lengths = random.sample(range(1,30), 2)
list0 = random.sample(range(1,100), list_lengths[0])
list1 = random.sample(range(1,100), list_lengths[1])

print(set([x for x in list0 if x in list1]))
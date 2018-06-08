# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# First attempt

ustr = input('Please enter a string: ').lower()
rstr = ustr[::-1]
if ustr == rstr:
	print('that is a Palindrome')
else:
	print('that is not a Palindrome')

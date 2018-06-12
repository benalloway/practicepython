# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

# First Attempt:

def getNumber(help_text="Give me a number: "):
	try:
		return int(input(help_text))
	except:
		return 00

def isPrime(i):
	if (i % 2 != 0 and i % 3 != 0) or i == 2 or i == 3:
		return True
	else:
		return False

if isPrime(getNumber()):
	print("That number is a prime number!")
else:
	print("That number is NOT prime")

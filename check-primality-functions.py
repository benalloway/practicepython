# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

# First Attempt:

def getNumber(help_text="Give me a number: "):
	return int(input(help_text))

def isPrime(i):
	isP = True
	if i > 1:
		for x in range(2, i):
			if (i % x) == 0:	
				isP = False
				break
	else:
		isP = False
	return isP

	
if isPrime(getNumber()):
	print("Number is prime")
else:
	print("Number is not prime")
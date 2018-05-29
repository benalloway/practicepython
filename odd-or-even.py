# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# 1) If the number is a multiple of 4, print out a different message
# 2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message


# first attempt, just the basics

# num = int(input("Please enter a number: "))

# if num % 2 == 0:
# 	print("You entered the number: " + str(num) + ". which is an even number")
# else:
# 	print("You entered the number: " + str(num) + ". which is an odd number")

# extra 1:

# num = int(input("Please enter a number: "))

# if num % 2 == 0:
# 	if num % 4 == 0:
# 		print("You entered the number: " + str(num) + ". which is an even number and is a multiple of 4")
# 	else:
# 		print("You entered the number: " + str(num) + ". which is an even number")
# else:
# 	print("You entered the number: " + str(num) + ". which is an odd number")

# extra 2:

num = int( input( "Please enter a number: " ) )
divideBy = int( input( "Please enter a number to divide by: " ) )

if num % 2 == 0:
	if num % 4 == 0:
		print( "You entered the number: " + str( num ) + ". which is an even number and is a multiple of 4" )
	else:
		print( "You entered the number: " + str( num ) + ". which is an even number" )
else:
	print("You entered the number: " + str( num ) + ". which is an odd number" )

if num % divideBy == 0:
	print( "And " + str( divideBy ) + " divides evenly into " + str( num ) )
else:
	print( "And " + str( divideBy ) + " does not divide evenly into " + str( num ) )
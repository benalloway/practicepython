# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
ran = random.randint(1, 9)
guesses = 0
while True:
	try:
		usr = input("Guess a number between 1 and 9! ")
		if usr == 'exit':
			print("Buh-Bye!")
			break
		
		usr = int(usr)

		if usr > 9 or usr < 1:
			guesses += 1
			print("You gotta enter a number between 1 and 9, silly")
		elif usr == ran:
			guesses += 1
			print("You guessed it in only " + str(guesses) + " guesses!")
			break
		elif usr > ran:
			guesses += 1
			print("You guessed to high... Guess again!")
		elif usr < ran:
			guesses += 1
			print("You guessed to low... Guess again!")
	except:
		guesses += 1
		print("You gotta enter a NUMBER, silly")

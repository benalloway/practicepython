# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
ran = random.randint(1, 9)
while True:
	try:
		usr = input("Guess a number between 1 and 9! ")
		if usr == 'quit':
			print("Buh-Bye!")
			break
		
		usr = int(usr)
		if usr > 9 or usr < 1:
			print("You gotta enter a number between 1 and 9, silly")
		elif usr == ran:
			print("YOU GOT IT!")
			break
		elif usr > ran:
			print("You guessed to high... Guess again!")
		elif usr < ran:
			print("You guessed to low... Guess again!")
	except:
		print("You gotta enter a NUMBER, silly")
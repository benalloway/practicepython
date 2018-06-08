# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:
# -	Rock beats scissors
# -	Scissors beats paper
# -	Paper beats rock

# First Attempt:

while True:
	print('Welcome to RockPaperScissors, a 2-player game built by Benjamin Alloway\nplease select from the following options: Rock, Paper or Scissors\n type exit to exit.')
	player1 = input('Player 1, enter your selection: ').lower()
	player2 = input('Player 2, enter your selection: ').lower()

	# edge casing
	if player1 == 'exit' or player2 == 'exit':
		break
	if player1 != 'rock' and player1 != 'paper' and player1 != 'scissors':
		print('\nPlayer 1, that is not an option\n')
	if player2 != 'rock' and player2 != 'paper' and player2 != 'scissors':
		print('\nPlayer 2, that is not an option\n')


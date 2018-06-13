# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# "My name is Michele"

# Then I would see the string:
# "Michele is name My"
# shown back to me.

# small line of code
# def gimmeString(string):
# 	print(string[::-1])

# gimmeString(input("enter a sentance: "))

# give me complexity!
def reverse(s):
	slist = s.split(" ")
	sreverse = []
	for x in range(len(slist)-1, -1, -1):
		sreverse.append(slist[x])
	print(" ".join(sreverse))

reverse(input("gimme a string: "))

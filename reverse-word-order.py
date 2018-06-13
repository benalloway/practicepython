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

# complexity

def reverse(s):
	string = []
	reverses = []
	for a in s:
		string.append(a)
	for x in range(string-1, -1, -1):
		reverses.append(string[x])
	print(reverses)

reverse(input("gimme a string"))

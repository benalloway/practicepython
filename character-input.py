# Exercise 1) 
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them when they will turn 100 years old.

# Extras:
# 1) Add on by asking the user for another nmber and printing out that many copies of the previous message (hint order of operations)
# 2) Print out that many copies of previous message on separate lines (hint "\n is the same as pressing the ENTER button)


# round 1 going for it
# name = input("Please enter your name ")
# age = input("and your age, please ")

# yearsToOneHundred = 100 - int(age)
# msg = "Hello " + name + ". You will be 100 years old in: " + str(yearsToOneHundred) + " years"

# print(msg)

# round 2 going for all the extras
name = input("Hello, \nplease enter your name: ")
age = int(input("Also, \nplease enter your age: "))
printNum = int(input("and, \nhow man times would you like to print this? "))
yearsToOneHundred = str(100 - age)

msg = "Hello " + name + ". You will be 100 in: " + yearsToOneHundred + " years. \n"

print(printNum * msg)
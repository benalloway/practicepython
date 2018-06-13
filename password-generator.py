# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:
# 1) Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

def password():
	choices2 = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	choices3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','&','*']
	password = ''
	
	while True:
		try:
			strength = int(input("Please input desired password strength between 1 and 3: "))
			if strength == 1:
				weakOptions = ['gravity', 'password', 'admin', 'root']
				password = random.choice(weakOptions)
				print("your new password is: " + str(password))
				break
			
			elif strength == 2:
				for x in range(random.randint(8,12)):
					password += random.choice(choices2)
				print("your new password is: " + str(password))
				break

			elif strength == 3:
				for x in range(random.randint(8,16)):
					password += random.choice(choices2)
					password += random.choice(choices3)
				print("your new password is: " + str(password))
				break

			else:
				print("\nplease select a number between 1 and 3\n")
		except:
			print("\nplease select a number between 1 and 3\n")

password()
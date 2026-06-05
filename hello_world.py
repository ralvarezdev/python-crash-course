#Hi! I'm Mister B
#This is my first code/code 0 while I learn Python, based on Chapter 2 of Python Crash Course
#I wish you enjoy it


#import this
	#Simple is better than complex.
	#Complex is better than complicated.
	#Readability counts.
	#There should be one-- and preferably only one --obvious way to do it.
	#Now is better than never.


name = input("What's your name? ")
print("What's up " + name.title() + "?")

print("\n\t\t\tActivating...\n")

#print(string(" or ') = output)
print("Hello World!")

#Variables:
message = "Hello Python Crash Course!"
print(message)

	#name = "ada lovelace"
	#print(name.title())
	
	#name = "ada lovelace"
	#print(name.lower())
	
	#name = "ada lovelace"
	#print(name.upper())

#Concatenation:
first_name = "mister"
last_name = "b"
full_name = first_name + " " + last_name
#print(full_name)
print("It's " + full_name.title() + "!")

#Languages that I'm going to learn \n (new line) \t (tabs)
print("\nThese are the first languages that I'm going to learn throughout my career:\n\tPython\n\tC\n\tC++")

#Stripping Whitespace:
favorite_language = ' python '
#favorite_language.rstrip()
#favorite_language.lstrip()
print("\nRight now, my favorite language is " + favorite_language.strip())

message = "One of Python's strengths is its diverse community."
print("\n" + message)

#Using input x2
famous_quote = '"A person who never made a mistake never tried anything new."'
print("\n\nFamous quote of the day:" + "\n\t" + "... once said, " + famous_quote)

question = input('\nWho do you think was "..."?' + " ")
full_name = "albert einstein"
print("\nSo, you said it was " + question.strip() + ". Well, it's an " + full_name.title() + "'s quote")

#Numbers + str = Characters
#Variables + str()
favorite_number = 5
print("\nDid you know my favorite number is " + str(favorite_number) + "?")

#Variables + str() + input
age = input("\n\nHow old are you? ")
print("Happy " + str(age) + " Birthday! Sorry for being late")

#Integers:
	#2+3
	#2-3
	#2/2
	#2*3
	#2**3
	#2+3*4

#Decimals/Floats:
	#2/3
	#0.4+0.4
	#0.2+0.1

question2 = input("\n\nDo you want to play with numbers? (y/N) ")
print("However, you'll do it. I'm your teacher!")

print("\nLet's play with numbers\n")
print("What's the result of the addition of 5 plus 3?")
print(5 + 3)

print("What's the result of the substraction of 11 less?")
print(11 - 3)

print("What's the result of the division of 64 by 8?")
print(64 / 8)

print("What's the result of the multiplication of 2 per 4?")
print(2 * 4)

print("What's the result of the number 2 with exponent 3?")
print(2 ** 3) 

print("What will happen if I put multiple operations in one expression?")
print(-8 + 2**4)

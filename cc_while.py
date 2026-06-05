#Hi! I'm Mister B
#This is my seventh code while I learn Python, based on Chapter 7 of Python Crash Course
#I wish you enjoy it

#The while Loop in Action

#current_number = 1
#while current_number <= 10000000:
#	print(current_number)
#	current_number += 1


#Letting the User Choose When to Quit
#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program "

#message = ""
#while message != 'quit':
#	message = input(prompt)
	
#	if message != 'quit':
#		print(message)


#active = True
#while active:
#	message = input(prompt)
	
#	if message == 'quit':
#		active = False
#	else:
#		print(message)

	
#while True;
#	city = input(prompt)
	
#	if city == 'quit':
#		break
#	else:
#		print("I'd love to go to " + city.title() + "!")


#Using continue in a Loop
#current_number = 0
#while current_number < 10:
#	current_number += 1
#	if current_number %2 == 0:
#		continue
	
#	print(current_number)


#Avoiding Infinite Loops
#x = 1
#while x <= 5
#	print(x)
#	x += 1

#This loops runs forever!
#x = 1
#while x <= 5:
#	print(x)

#y = 1
#while y >=1:
#	print(y)
#	y += 1


#Using while Loops with Lists and Dictionaries

#Start with users that need to be verifid,
#and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#Verify each user until there are no more unconfirmed users
#Move each verified user into the list of confirmed users
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
	
#Display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

print("\n")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
	
print(pets)

print("\n")

#Filling a Dictionary with User Input
responses = {}

#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
	#Prompt for the person's name and response
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	
	#Store the response in the dictionary
	responses[name] = response
	
	#Find out if anyone else is going to take the poll
	repeat = input("Would you like to let another person respond? (yes\ no) ")
	if repeat == 'no':
		polling_active = False
		
#Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response)

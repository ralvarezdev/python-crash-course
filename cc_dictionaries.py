#Hi! I'm Mister B
#This is my fifth code while I learn Python, based on Chapter 6 of Python Crash Course
#I wish you enjoy it

#Dictionaries. They use key-values

#A Simple Dictionary
#Braces: {}
alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])

new_points = alien_0['points']
print("You have earned " + str(new_points) + " points")

#OOP
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\n")

#Modifying Values in a Dicitonary
print("The alien is " + alien_0['color'])

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'])

print("\n")

alien_0['speed'] = 'medium'
print("Original x-position: " + str(alien_0['x_position']))

#Move the alien to the right
#Determine how far to move the alien base on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien
	x_increment = 3
	
#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#Removing Key-Value Pairs
del alien_0['points']
print(alien_0)

print("\n")

#A Dictionary of Similar Objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("Sarah's favorite language is " + favorite_languages['sarah'].title())

#Looping Through a Dictionary

#Looping Through All Key-Value Pairs
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
	
for k, v in user_0.items():
	print("\nKey: " + k)
	print("Value: " + v)

print("\n")

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title())

print("\n")

for name in favorite_languages:
	print(name.title() + "'s favorite language is " + language.title())

print("\n")

friends = ['sarah', 'phil']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " 
		+ favorite_languages[name].title()  + "!")

print("\n")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

print("\n")

#Looping Through a Dictionary's Keys in Order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll")

print("\n")

#Looping Through All Values in a Dicionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print("\n")

#To see each language chosen without repetition, we can use a set. It's pretty
#similar to a list
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

print("\n")
 

#Nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow','points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
	
print("\n")

#Make an empty list for storing aliens
aliens = []

#Make 25 green aliens
for alien_number in range(5):
	yellow_alien = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
	aliens.append(yellow_alien)
for alien_number in range(25):
	green_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(green_alien)


#Change the first three aliens to yellow, medium-speed aliens worth 10 points
#each
for alien in aliens[0:15]:
	if alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
	elif alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

	
#Show the first 5 aliens
for alien in aliens[:30]:
	print(alien)
print("...")
		
#Show how many aliens have been created
print("\nTotal number of aliens " + str(len(aliens)))

print("\n")

#A List in a Dictionary
#Store information about a pizza being ordered
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
	
#Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
	}

for name, languages in favorite_languages.items():
	if len(languages) >=2:
		print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())
	elif len(languages) <=1:
		print("\n" + name.title() + "'s favorite language is:")
		for language in languages:
			print("\t" + language.title())

#A Dictionary in a Dictionary
users = {
	'aenstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princenton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())

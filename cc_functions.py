#Hi! I'm Mister B
#This is my eighth code while I learn Python, based on Chapter 8 of Python Crash Course
#I wish you enjoy it

def greet_user(): #function definition
	"""Display a simple greeting""" #docstring
	print("Hello!")

greet_user()

#Passing Information to a Function

def greet_user(username): #parameter
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")
	
greet_user('jesse') #argument


#Passing Arguments

#Positional Arguments + Multiple Funciton Calls
def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have a " + animal_type)
	print("My " + animal_type + "'s name is " + pet_name.title())
	
describe_pet('dog', 'luna')
describe_pet('hamster', 'willie')

#Keyword Arguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have a " + animal_type)
	print("My " + animal_type + "'s name is " + pet_name.title())
	
describe_pet(pet_name='luna', animal_type='dog')

#Default Values (this works as a positional arument)
def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet"""
	print("\nI have a " + animal_type)
	print("My " + animal_type + "'s name is " + pet_name.title())
	
describe_pet(pet_name='luna')
describe_pet('luna')
describe_pet(pet_name='willie', animal_type='hamster')
describe_pet('willie', 'hamster')
describe_pet(animal_type='hamster', pet_name='willie')

print("\n")


#Return Values

#Returning a Simple Value
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=' '):
	"""Return a full name, neatly formatted"""
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
musician = get_formatted_name('john', 'hooker', 'lee')

#Returning a Dictionary
def build_person(first_name, last_name, age=' '):
	"""Return a dictionary of information about a person"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print("\n")


#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = first_name + " " + last_name
	return fullname.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break
		
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

print("\n")


#Passing a List
def greet_users(names):
	"""Print a simple greeting to each user in the list"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print("\n")

#Modifying a list in a Function
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	
	print("Printing model: " + current_design)
	completed_models.append(current_design)

print("\nThe folowing models have been printed:")
for completed_model in completed_models:
	print(completed_model)

print("\n")


#Code more efficient
def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#Simulate creating a 3D print from the design
		print("Printing model: " + current_design)
		completed_models.append(current_design)

#A function should be designed for one specific job
def show_completed_models(completed_models):
	"""Show all models that were printed"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Preventing a Function from Modifying a List
	#function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)

print("\n")


#Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
	"""Print the List of toppings that have been requested"""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
	"""Summarize the pizza we are about to make"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Making Positional and Arbitary Arguments
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make"""
	print("\nMaking a " + str(size) + 
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n")

#Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] =value
	return profile

user_profile = build_profile('albert', 'einstein', 
							location='princeton', 
							field='physics')

print(user_profile)


#Storing Your Functions in Modules
	#module_name.function_name()
import cc_modules

cc_modules.make_pizza(16, 'pepperoni')
cc_modules.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Importing Specific Functions
	#from module_name import function_name
	#from module_name import function_0, function_1, function_2
from cc_modules import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to Give a Function an Alias
	#from module_name import function_name as fn
from cc-modules import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to Give a Module an Alias
import cc_modules as m

m.make_pizza(16, 'pepperoni')
m.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Importing All Functions in a Module
	#from module_name import *
from cc_modules import *


#Styling Functions
	#Functions should have descriptive names, and these names should use 
	#lowercase letters and underscores
	
	#Every function should have a comment that explains concisely what the
	#function does
	
	#If you specify a default value for a parameter, no spaces should be used
	#on either side of the equal sign:
	#def function_name(parameter=0, parameter_1='default value')
	
	#The same convention should be used for keyword arguments in function 
	#calls:
	#function_name(value_0, parameter_1='value')
	
	#PEP recommends that you limit lines of code to 79 characters so every
	#line is visible in a reasonably sized editor window
	#def function_name(
	#		parameter_0, parameter_1, parameter_2, 
	#		parameter_3, parameter_4, parameter_5):
	#	function body...
	
	#If your program or module has more than one function, you can separate
	#each by two blank lines to make it easier to see where one function ends
	#and the next one begins
	
	#All import statements should be written at the beginning of a file.
	#The only exception is if you use comments at the beginning of your file
	#to describe the overall program

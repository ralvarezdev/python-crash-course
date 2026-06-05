#Hi! I'm Mister B
#This is my fourth code while I learn Python, based on Chapter 5 of Python Crash Course
#I wish you enjoy it


#If Statements

#Simple Example
#Square brackets: []
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.lower())
	
	
#Conditional Tests / Boolean Expressions (A Boolean value is ether True or False)

#Checking for Equality
car = 'bmw'
car == 'bmw'
#True

car = 'audi'
car == 'bmw'
#False

#Ignoring Case When Checking for Equality
car = 'Audi'
car.lower() == 'audi'
#True
car
#'Audi'

print("\n")

#Checking for Inequality. ! represents not. != is not
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")

print("\n")

#Magic number
answer = 17

if answer != 42:
	print("That is not the correct answer. Please try again!")
	
print("\n")

age = 19
age < 21
#True
age <= 21
#True
age > 21
#False
age >= 21
#False


#Checking Multiple Conditions

#Using and to Check Multiple Conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >=21
#False
age_0 = 22
age_1 = 21
age_0 >= 21 and age_1 >=21
#True

#Using or to Check Multiple Conditions
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
#True
age_0 = 18
age_0 >= 21 or age_1 >= 21
#False

#You can add parenthesis to improve readability
(age_0 >= 21) and (age_1 >= 21)

#Checking Wether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
#True
'pepperoni' in requested_toppings
#False

#Is the game running?
game_active = True
#Can a user edit certain content on a website?
can_edit = False


#Simple if Statement
#if conditional_test:
#	do something
	
age = 19
if age >= 18:
	print("You're old enough to vote!")
	print("Have you registered to vote yet?")
	
#if-else Statements
age = 17
if age >= 18:
	print("You're old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you're too young to vote")
	print("Please register to vote as soon as you turn 18!")

print("\n")

#The if-elif-else Chain
age = 12

if age < 4:
	print("Your admission cost is $0")
elif age < 18:
	print("Your admission cost is $5")
else:
	print("Your admission cost is $10")

#More efficient code, the purpose is narrower
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
	
print("Your admission cost is $" + str(price))

#Using Multiple elif Blocks
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
	
print("Your admission cost is $" + str(price))

#Omitting the else Block. The else block is a catchall statement
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5
	
print("Your admission cost is $" + str(price))

print("\n")

#Testing Multiple Conditions

#Someone requests a two-topping pizza
request_toppins = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese")

print("\nFinished making your pizza!")


#Using if Statements with Lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print("Sorry, we are out of green peppers right now")
		else:
			print("\nAdding " + requested_topping + "...\n")
	print("\nFished making your pizza!")
	
#If the list is empty
else:
	print("Are you sure you want a plain pizza?")

print("\n")

#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 
'pepperoni', 'pineapple',  'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + "...\n")
	else:
		print("Sorry, we don't have " + requested_topping + "\n")
		
print("\nFinished making yourpizza!")

#Single space around comparison operators, such as ==, >=, <=
#if age < 4
#Is better than:
#if age>4

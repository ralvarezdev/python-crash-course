#Hi! I'm Mister B
#This is my ninth code while I learn Python, based on Chapter 8 of Python Crash Course
#I wish you enjoy it

#Moldules
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make"""
	print("\nMaking a " + str(size) + 
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

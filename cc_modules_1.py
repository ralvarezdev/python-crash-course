#Hi! I'm Mister B
#This is my twelveth code while I learn Python, based on Chapter 9 of Python Crash Course
#I wish you enjoy it


#Importing a Module into a Module
"""A class that can be used to represent a car"""

class Car():
	"""A simple attempt to represent a car"""
	
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		#Setting a Default Value for an Attribute
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage"""
		print("This car has " + str(self.odometer_reading) + " miles on it")
	
	#Modifying Attribute Values 
	#Modifying an Attribute's Value Through a Method
	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading"""
		self.odometer_reading += miles


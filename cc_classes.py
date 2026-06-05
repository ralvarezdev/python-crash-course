#Hi! I'm Mister B
#This is my tenth code while I learn Python, based on Chapter 9 of Python Crash Course
#I wish you enjoy it


#Classes #the superclass
#Object-oriented programming is one of the most effective approaches to writing
#software

#Making an object from a class is called instantiation


#Creating and Using a Class

#Creating the Dog Class
class Dog(): #Capitalized names refer to classes in Python
	"""A simple attempt to model a dog"""
	
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age
	
	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(self.name.title() + " is now sitting")
	
	def roll_over(self):
		"""Simulate a dog sitting in response to a command"""
		print(self.name.title() + " rolled over!")

#The __init__() Method #A function that's part of class is called a method

#Making an Instance from a Class
my_dog = Dog('luna', 6)

print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old")

#Accessing Attributes #my_dog.name

#Calling Methods
my_dog.sit()
my_dog.roll_over()

print("\n")

#Creating Multiple Instances
your_dog = Dog('lucy', 3)
cc_dog = Dog('willie', 6)

print("Your dog's name is " + your_dog.name.title())
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()
print("\nCrash Course dog's name is " + cc_dog.name.title())
print("Crash Course dog is " + str(cc_dog.age) + " years old")
cc_dog.roll_over()

print("\n")


#Working with Classes and Instances

#The Car Class
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

my_new_car = Car('audi', 'a4', '2016')

print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading = 23 #Modifying an Attribute's Value Directly
my_new_car.update_odometer(23) #Modifying an Attribute's Value Through a Method
my_new_car.read_odometer()

print("\n")

my_used_car = Car('subaru', 'outback', 2013)

print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print("\n")


#Inheritance #a subclass

#the __init__() ethod for a Child Class
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles"""
	
	def __init__(self, make, model, year):
		"""
		Initialize atributes of the parent class.
		Then initialize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		#Defining Attributes and Methods for the Child Class
		self.battery_size = 70
	
	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print("This car has a " + str(self.battery_size) + "-KWh battery")

	#Overriding Methods from the Parent Class
	def fill_gas_tank():
		"""Electric cars don't have gas tanks"""
		print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

print("\n")

#Instances as Attributes
class Battery():
	"""A simple attempt to model a battery for an electric car"""
	
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Print a statement describing the battery size"""
		print("This car has a " + str(self.battery_size) + "-KWh battery")
	
	def get_range(self):
		"""Print a statement about the range this battery provides"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge"
		print(message)

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles"""
	
	def __init__(self, make, model, year):
		"""
		Initialize atributes of the parent class.
		Then initialize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n")

#Modeling Real-World Objects

#Efficiency
#Different approaches
#Focus more on real-world questions than syntax-focused questions
#You'll rewrite many times a class or part of a code to get it working
#That's completely normal
#When a code works, you'll find the simpler and more efficient code by a matter
#of time. Don't punish yourself of things 
#you don't have control of [creativity]


#Importing lasses

#Importing a Single Class
from cc_modules_0 import Car

my_new_car = Car('audi', 'a4', '2016')

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

print("\n")

#Importing Multiple Classes from a Module
from cc_modules_0 import Car, ElectricCar

my_new_car = Car('audi', 'a4', '2016')

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

print("\n")

my_beetle = Car('volkswagen', 'beetle', 2016)

print(my_beetle.get_descriptive_name())

print("\n")

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n")

my_tesla = ElectricCar('tesla', 'roadster', 2016)

print(my_tesla.get_descriptive_name())

print("\n")

#Import an Entire Module
#import cc_modules_0.py

#Importing All Classes from a Module
#from module_name import * #this method is not recommended for two reasons:
#Reading, clearness of the classes a program uses and you can accidentally
#import a class with the same name as something else in your program file

#Importing a Module into a Module
from cc_modules_1 import Car
from cc_modules_2 import Battery, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

print("\n")

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

#Fin Your Own Workflow


#The Python Standard Library
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title())

#The module random contains functions that generate random numbers in a variety of ways
#The function randint() returns an intenger in the range you provide
from random import radint
x = randint(1, 6)

#Python Module of the Week: http://pymotw.com/


#Styling Classes

#Class names should be written in CamelCaps
#Every class should have a docstring inmediately following the class definition.
#You can use blank lines to organize code, but don't use them excesively
#Within a c;ass you can use one blank line between methods, and within a module
#you can use two blank lines to separate classes
#If you need to import a module from the standard library and a module that
#you wrote, place the import statement for the standard library module first.
#then add a blank line and the import statement for the module you wrote

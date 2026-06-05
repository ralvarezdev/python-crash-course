#Hi! I'm Mister B
#This is my third code while I learn Python, based on Chapter 4 of Python Crash Course
#I wish you enjoy it

#Looping
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    #Doing More Work Within a for Loop
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + "\n")
    
#Doing Something After a for Loop
print("Thank you, everyone. That was a great magic show!")

print("\n")


#Making Numerical Lists

#Using the range() Function
for value in range(1,5):
	print(value)
	
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

print("\n")

squares = []
for value in range(1,11):
	square = value**2
	#This is sometimes unnecessary
	squares.append(square)
	
print(squares)

print("\n")

#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

print(str(min(digits)))
print(str(max(digits)))
print(str(sum(digits)))

print("\n")

#Summing a Million
numbers = list(range(1,1000000))
print(numbers)
print(str(sum(numbers)))

print("\n")

#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])

print("\n")

#Looping Through a Slice
print("Here are the first three players on my team")
for player in players[:3]:
	print(player.title())

print("\n")

	
#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
#This doesn't work:
#friend_foods = my_foods
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")

#Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Looping Through All Values in a Tuple
for dimension in dimensions:
	print(dimension)

print("\n")

#Writing over a Tuple
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)


#Style Guidelines
#https://python.org/dev/peps/pep-0008/
#Python Enhancement Proposal (PEP)
#Indentation = 4 spaces
#Each line should be less than  80 characters
#All comments should be limit to 72 characters per line
#You should not place th or four blank lines between two sections

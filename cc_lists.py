#Hi! I'm Mister B
#This is my second code while I learn Python, based on Chapter 2 and 3 of Python Crash Course
#I wish you enjoy it


#Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accesing Elements in a list
print(bicycles[0])

print(bicycles[0].title())

#Index Positions Start at 0, Not 1
print(bicycles[1])
print(bicycles[2])

#Last item
print(bicycles[-1])

#Using Individual values form a List
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

print("\n")


#Modifying Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Appending Elements to the End of a List
motorcycles.append('ducati')
print(motorcycles)

print("\n")

food = []

food.append('apples')
food.append('bananas')
food.append('beans')

print(food)

#Inserting Elements into a List
food.insert(0, 'carrots')
print(food)

#Removing an Item using the del Statement

del food[0]
print(food)

#Removing an Item using the pop() Method
popped_food = food.pop(1)
print(popped_food)

print("The last food I bought was a pair of " + popped_food.lower())

print("\n")

#Removing an Item by Value
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + "is too expensive for my preference")

print("\n")


#Organizing a list

#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("\n")

#Sorting a List Temporarily with the sorted() Function
print("Here's the original list:")
print(cars)

print("\nHere's the sorted list:")
print(sorted(cars))

print("\nHere's the original list:")
print(cars)

#Printing a List in Reverse Order
cars.reverse()
print(cars)

print("\n")

#Finding the Length of a List
len(cars)
print(str(len(cars)))

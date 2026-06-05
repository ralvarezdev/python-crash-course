#Hi! I'm Mister B
#This is my sixth code while I learn Python, based on Chapter 7 of Python Crash Course
#I wish you enjoy it

#Using int() to Accept String Input

#name = input("Please enter your name: ")
#print("Hello, " + name.title() + "!")

prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat's your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Using int() to Accept Numerical Input
age = input("\nHow old are you? ")
age = int(age)
if age >= 18:
	print("Adult")

height = input("How tal are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou're tall enough to ride!")
elif height <= 35:
	print("\nYou'll be able to ride when you're a little older")

#The Modulo Operator (%)
#which divides one number by another number and returns the remainder
4 % 3
#1
6 % 3
#0

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number %2 == 0:
	print("\nThe number " + str(number) + " is even")
else:
	print("\nThe number " + str(number) + " is odd")

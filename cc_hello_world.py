#Hi! I'm Mister B
#This is my first code while I learn Python, based on Chapter 2 of Python Crash Course
#I wish you enjoy it

print("Hello World!")


#Naming and Variables
message = "Hello Python world!"
print(message)

message = "Hello python Crash Course world!"
print(message)

print('This is a string')
print("This is also a string")

#'I told my friend, "Python is my favorite language!"'
#"The language 'Python' is named after Monty Python, not the snake."
#"One of Python's strengths is its diverse and supportive community."


#Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.lower())
print(name.upper())


#Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

print("Hello, " + full_name.title() + "!")


#Adding Whitespace to Strings with Tabs or Newlines
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping space
favorite_language = ' python '
print("\n" + favorite_language.rstrip() + "\n" + favorite_language.lstrip() + "\n" + favorite_language.strip())

print("\n")


#Numbers
print(2+3)
print(2-3)
print(2/3)
print(2*2)
print(2**3)
print(2+4/3)
print(((2+4)+5)/3)

print("\n")

#str() Function
age = 23
message = "Happy " + str(age) + "rd Birhtday!"

print(message)

print("\n")


#Zen of Python
import this

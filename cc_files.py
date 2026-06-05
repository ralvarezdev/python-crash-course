#Hi! I'm Mister B
#This is my eleventh code while I learn Python, based on Chapter 10 of Python Crash Course
#I wish you enjoy it

#Files and Exceptions

#with open('folder/filename.txt') as file_object:
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

#Absolute Paths

#Linux
#file_path = '/home/.../.../filename.txt'
#with open(file_path) as file_object:

#Windows
#file_path = 'C:\Users\...\...\file_name.txt'
#with open(file_path) as file_object:

#Reading Line by Line

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#Making a List of Lines from a File

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

#Working with a File's Contents

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))
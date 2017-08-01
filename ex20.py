# imports argv module from sys
from sys import argv

# arguments to passed to argv
script, input_file = argv

# define a function
def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

# function print_a_line takes two arguments
def print_a_line(line_count, f):
	print line_count, f.readline()

#current_file is open input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# current_file is argument of print_all function
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# 1 is assigned to current_line
current_line = 1
print_a_line(current_line, current_file)

# current_line is incremented by 1 over its previous value
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
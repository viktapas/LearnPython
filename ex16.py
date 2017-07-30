# import argv module from sys
from sys import argv

# assign argv input to script and filename in right order
script, filename = argv

# prints strings
print """
	We're going to erase %r." % filename
	If you don't want that, hit CTRL+C (^C).
	If you do want that, hit RETURN.
	"""

# waiting for input from user
raw_input("? ")

# print string
print "Opening the file..."
# opens 'filename' and assign to 'target'
target = open(filename, 'w')
print "Truncating the file. Good bye!"
# truncate variabel 'target' and eventually truncates opened filename
target.truncate()

print "Now I'm going to ask you for three lines."

#raw inputs from the user
line1 =  raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write line1, line 2, line3 to filename
target.write('%r\n%r\n%r' %(line1, line2, line3))

print "And finally, we close it."
# close filename
target.close()
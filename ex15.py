# import module argv from sys
from sys import argv

#assigning argv inputs to script and filename
script, filename = argv

# opens the filename and assigns to variable 'txt'
txt = open(filename)

# prints the filename in raw format (%r) alongwith the string
print "Here's your file %r:" % filename
# tells to read 'txt' with no arguments
print txt.read()

# prints string
print "Type the filename again:"
# assigns input to 'file_again' variable in raw format
file_again = raw_input("> ")

# opens the file 'file_again'
txt_again = open(file_again)

# reads variable 'txt_again' with no argument
print txt_again.read()
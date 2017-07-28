# Formatted variable '%d' is inside string and is assigned value 10 using
# percent character.
x = "There are %d types of people." % 10
# 'binary' variable is assigned string 'binary'.
binary = "binary"
# 'do_not' variable is assigned string 'don't'.
do_not = "don't"
# 'y' variable is assigned a string inside which are two formatted variables(%s, %s)
# and are assigned 'binary' and 'do_not' respectively.
y = "Those who know %s and those who %s." %(binary, do_not)

# Print variable x.
print x
# Print variable y.
print y

# Value of variable 'x' is assigned to formatted variable '%r' inside string
# and string is print.
print "I said: %r." % x
# Value of variable 'y' is assigned to formatted variable '%s' inside string
# and string is print.
print "I also said: '%s'." % y

# Variable 'hilarious' is assigned False.
hilarious = False
# Formatted variablel '%r' is inside string which is assigned to variable 'joke_evaluation'.
joke_evaluation = "Isn't that joke so funny?! %r"

# Print remainder of joke_evaluation to hilarious.
print joke_evaluation % hilarious

# A string is assigned to variable 'w'.
w = "This is the left side of..."

# A string is assigned to variable 'e'.
e = "a string with a right side."

# Python 2 treats strings special when used with '+' operand.
print w + e
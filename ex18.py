# making function def
def print_two(*args):
	# unpacks the arguments
	arg1, arg2 = args
	# printing arguments
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

# this function has no argument
def print_none():
	print "I got nothing."


print_two("dzen", "vikas")
print_two_again("dzen", "vikas")
print_one("First!")
print_none()
i = 0
numbers = []

# changed while-loop into function that can be called
def list(i):
	while i < 6:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i +1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

# function called
print list(i)

print "The numbers: "

for num in numbers:
	print num
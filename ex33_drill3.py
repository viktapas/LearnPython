i = 0
incement = 2

numbers = []

def loop(i, incement):
	while i < 10:
		print "At the top i is: %d" % i
		numbers.append(i)

		i += incement
		print "Numbers row: ", numbers
		print "At the bottom i is: %d" % i

print loop(i, incement)

print "The numbers: "

for i in numbers:
	print i



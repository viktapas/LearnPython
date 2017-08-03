i = 0

numbers = []

def loop(i):
	while i < 10:
		print "At the top i is: %d" % i
		numbers.append(i)

		i += 1
		print "Numbers row: ", numbers
		print "At the bottom i is: %d" % i

print loop(i)

print "The numbers: "

for i in numbers:
	print i



i = 0

numbers = []

def loop(i):
	for i in range(0, 7, 1):
		print "At the top i is: %d" % i
		numbers.append(i)

		print "Numbers row: ", numbers
		print "At the bottom i is: %d" % i

print loop(i)

print "The numbers: "

for i in numbers:
	print i

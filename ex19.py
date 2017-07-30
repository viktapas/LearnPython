# make a function 'cheese_and_crackers' using def for define
# cheese_and_crackers is function
# cheese_count and boxes_of_crackers are arguments
# arguments' values are not passed directly
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# arguments' values are passed directly to the function
cheese_and_crackers(20,30)


print "OR, we can use variables from our script:"
# arguments' values are passed using function's variables
amount_of_cheese = 10
amount_of_crackers = 50

# cheese_and_crackers runs
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# arguments' vlaues are passed directly but with math
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# arguments' values are passed using variables and math combined
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# assign value to variables
people = 300
cars = 250
buses = 350

# if cars value are greater than people's
if cars > people:
	print "We should take the cars."
# else--if cars are less than people
elif cars < people:
	print "We should not take the cars."
# else print this	
else:
	print "We can't deccide."

#if buses greater than cars
if buses > cars:
	print"That's too many buses."
# else--if buses are less than cars print this
elif buses < cars:
	print "May be we could take the busese."
# else print this
else:
	print "We still can't decide."

# if people are greater than buses, print this
if people > buses:
	print "Alright, let's just take the buses."
# else print this
else:
	print "Fine, let's stay home then."

#if people are less than buses and people are greater than cars, print this
if people < buses and people > cars:
	print "Alright, let's just take the cars."

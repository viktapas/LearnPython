people = 300
cars = 250
buses = 350


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't deccide."

if buses > cars:
	print"That's too many buses."
elif buses < cars:
	print "May be we could take the busese."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

if people < buses and people > cars:
	print "Alright, let's just take the cars."

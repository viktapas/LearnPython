# Total number of available cars assigned to "cars"
cars = 100
# number of passangers a car can accomodate
space_in_a_car = 4.0
# number of drivers available
drivers = 30
# total number of passangers
passangers = 90
# Number of empty cars
cars_not_driven = cars - drivers
# Number of cars driven
cars_driven = drivers
# Number of people can be transported
carpool_capacity = cars_driven * space_in_a_car
# Number of passangers to be put in each car
average_passangers_per_car = passangers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passangers, "to carpool today."
print "We need to put about", average_passangers_per_car, "in each car."
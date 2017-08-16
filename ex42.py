## Animal is-a object
class Animal(object):
	pass

# Dog is-a object of class Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name of some kind
		self.name = name

## Cat is-a object of class Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name 'name'
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name 'name'
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a object of class Person
class Employee(Person):

	def __init__(self, name, salary):
		##
		super(Employee, self).__init__(name)
		## Employee has-a salary 'salary'
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a object
class Salmon(Fish):
	pass

## Halibut is-a object
class Halibut(Fish):
	pass


## rover is-a Dog named "Rover"
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet 'satan'
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet 'rover'
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is a Hailbut
harry = Hailbut()
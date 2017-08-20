# ex44e.py


# Define Global variables etc here.....
m_number = 100	#Global variable

class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(Other):

	var1= 50

	def __init__(self, number, name):
		# print self
		self.m_number = number
		print self.m_number		# This is calling the local-scope variable named 'm_number'

		print m_number	# ERROR: b'coz this is calling the Global variable named 'm_number'
						# but there is no Global variable named 'm_named' is defined 
		m_name = name 	
		print m_name

		#self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		super(Other, self).altered()
		print "CHILD, AFTER OTHER altered()"

son = Child(12, 'vikas')
# Child().__init__(self, 12, 'vikas')
beta = Child(23, 'vikku')
print son
print son.m_number
print son.var1
print m_number
print beta
#print son.m_name
# son.implicit()
# son.override()
# son.altered()
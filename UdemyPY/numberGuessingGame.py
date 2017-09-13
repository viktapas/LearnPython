import random

#a list
guesses = []

random_number = random.randint(1, 70)

user_guess = int(raw_input("Enter a number b/w 1 and 70: "))
#adding user's guess to list 'guesses'
guesses.append(user_guess)

while user_guess != random_number:
	if user_guess > random_number:
		print "Number is high!"
	else:
		print "Number is low!"
		
	guesses.append(user_guess)
	user_guess = int(raw_input("Enter a number b/w 1 and 70: "))



else:
	print "*"*60
	print "Hurray! You got it right."
	print "It took you %i guesses to reach the number. Good job!" %len(guesses)
	print  "Your guess log: "+ str(guesses)
	print "*"*60
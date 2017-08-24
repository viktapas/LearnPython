# ex45a.py


from sys import exit
from random import randint

# Introduce the player to the game.
print "Hi gamer. I'm gonna guide you through this caspsule"
print "and will try help you escape this death."
print "Lets face the reality. You are being chased by a danger. The capsule"
print "you are in is going to blast due to malfunctions."
print "Now you have two options: either you die or escape."
print "Ofcourse you are gonna try escape. You have no time to"
print "waste so; runnn.....!"


class scene(object):
	"""docstring for scene"""
	def enter(self):
		print "This scene is not yet configured."
		print "Sublclass it and use enter()."
		exit(1)


class GameEngine(object):
	def __init__(self, scene_map):
		self.a_scene_map = scene_map

	def play(self):
		current_scene = self.a_scene_map.opening_scene()

		while True:
			print "\n-----------------------"
			next_scene_name = current_scene.enter()
			current_scene = self.a_scene_map.next_scene(next_scene_name)


class CentralCorridor(scene):

	def enter(self):
		print "You now have reached the 'central corridor'."
		print "Here are three rooms:"
		print "#1 Dragon room"
		print "#2 Aligator room"
		print "#3 Fire room"
		print "and you have to choose any one to enter the next step. Hurry!!"

		action = raw_input("Enter the room #> ")

		if int(action) == 1:
			return 'dragon_room'

		elif int(action) == 2:
			return 'aligator_room'

		elif int(action) == 3:
			return 'lava_room'

		else:
			print "You choose to die. The capsule blasted and you died."
			exit(1)


class DragonRoom(scene):

	def enter(self):
		print "Dragon: Welcome to the dragon room. Hahaha..."
		print "There is no going back.Ohaha...!"
		print "I'm not gonna let you take my gold box. Instead"
		print "I'm going to taste you this lunch. Yummy!"

		print "Don't listen him. You can kill this dragon"
		print "only with dzen sword,a boss level sword, and can collect"
		print "the gold box and exit the room."

		print "Guess the sword number (1 to 3) to get the dzen sword."
		print "You have two chances."

		sword = randint(1,3)
		count = 1

		guess = raw_input("Input the sword no.> ")

		if guess == sword and count < 3:
			print "Congrats! You killed the dragon and took the gold box."
			return 'escape_capsule'

		else:
			print "You died. My puppy is better at this."
			exit(1)


class AligatorRoom(scene):

	def enter(self):
		print "***YOU ENTERED THE ALIGATOR ROOM***"
		print "Aligators: You child fall in wrong pit. HeyHeyHey..."
		print "Good thing is you can't escape us. HeyHeyHey...!"
		print "You smells yummy."
		print "We're going to taste you this dinner. Yummy!"

		print "Don't listen him. You can't kill these hungry"
		print "bostards. However you can escape by boarding the boat."
		print "Let's just get out of the trouble. You have to enter a"
		print " b/w 1 and 3 and if your guess turns out false, you die."
		print "Good luck!"

		good_boat = randint(1,3)
		guess = raw_input("[boat #]> ")

		if int(guess) != good_boat:
			print "You jump into the boat #%r. and got eaten by aligators." % guess
			print "They enjoyed you a lot. YOU DIED!"
			exit(1)

		else:
			print "Congrats! You entered the right boat #%r and" % guess
			print "successfuly passed the aligators."
			return 'escape_capsule'


class LavaRoom(scene):
	
	def enter(self):
		print "***YOU ENTERED THE LAVA ROOM***"
		print "You entered the lava room. Its hot and the whole floor is lava."
		print "However, there is a good news, here are 3 bridges out of which"
		print "one is free of fault. You have to choose one. Faulty bridges will"
		print "collapse and you will get eaten by the lave.You have two chance."
		print "Have a nice guess!"

		guess = raw_input("Enter the bridge #> ")
		count = 1
		good_bridge = randint(1,4)

		while int(guess) != good_bridge and count < 2:
			print "This is your **last chance**. Good luck!"
			guess = raw_input("Enter the bridge #> ")

		if int(guess) == good_bridge and count < 2:
			print "You are amazing! You chose the right bridge."
			return 'escape_capsule'

		else:
			print "Damn, you chose the wrong bridge and died. Sad."
			exit(1)


class EscapeCapsule(scene):

	def enter(self):
		print "Good job so far. Now you have to enter the correct 1-digit code"
		print "(from 1 to 3) to open the capsule and escape."
		print "You have 2 chance to input correct code."
		action = raw_input("Enter the code:> ")
		count = 1
		code = randint(1,3)

		while int(action) != code and count < 2:
			print "This is your LAST chance. Good luck!"
			action = raw_input("Enter the code:> ")
			count += 1

		if int(action) == code and count < 2:
			print "\n***********"
			print "CONGRATULATIONS! YOU WON THE GAME!!!"
			print "\n***********"
			exit(1)

		else:
			print "You failed the last moment. You died. :("
			exit(1)


class Map(object):
	scenes = {
		'aligator_room': AligatorRoom(),
		'dragon_room': DragonRoom(),
		'lava_room': LavaRoom(),
		'central_corridor': CentralCorridor(),
		'escape_capsule': EscapeCapsule()
	}

	def __init__(self, start_scene):
		self.m_start_scene = start_scene

	def next_scene(self, scene_name):
		return self.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.m_start_scene)


a_map = Map('central_corridor')
a_game_engine = GameEngine(a_map)
a_game_engine.play()

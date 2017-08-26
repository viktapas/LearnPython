# ex45a.py

import ex45b


class GameEngine(object):
	def __init__(self, scene_map):
		self.a_scene_map = scene_map

	def play(self):
		current_scene = self.a_scene_map.opening_scene()

		while True:
			print "\n-----------------------"
			next_scene_name = current_scene.enter()
			current_scene = self.a_scene_map.next_scene(next_scene_name)




class Map(object):
	scenes = {
		'aligator_room': ex45b.AligatorRoom(),
		'dragon_room': ex45b.DragonRoom(),
		'lava_room': ex45b.LavaRoom(),
		'central_corridor': ex45b.CentralCorridor(),
		'escape_capsule': ex45b.EscapeCapsule()
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

import pygame
import numpy
import const.screen
import movement.steering
import movement.kinematic

def arrow_move(max_speed):
	def _arrow_move(update):
		def __arrow_move(self, key):
			direction = numpy.array([0, 0])
			if key[pygame.K_UP]:
				direction += [0, -1]
			if key[pygame.K_DOWN]:
				direction += [0, 1]
			if key[pygame.K_LEFT]:
				direction += [-1, 0]
			if key[pygame.K_RIGHT]:
				direction += [1, 0]
			
			self.steering.linear = numpy.asarray(direction) * 100
			self.kinematic.update(self.steering, max_speed, 1 / const.screen.FRAME_RATE)
			update(self, key)
		return __arrow_move
	return _arrow_move

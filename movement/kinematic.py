import numpy as np
from movement.steering import Steering
from math import isnan
import const
class Kinematic(object):
	"""docstring for Kinematic"""
	def __init__(self):
		super().__init__()
		self.position = np.zeros([2,], float)
		self.orientation = float(0)
		self.velocity = np.zeros([2,], float)
		self.rotation = float(0)
	def velocity2orientation(self, velocity):
		if velocity[1] == 0:
			orientation = 0 if velocity[0] == 0 else (np.pi / 2 if velocity[0] < 0 else -np.pi / 2)
		else:
			orientation = np.arctan(velocity[0] / velocity[1])
		orientation += np.pi if velocity[1] > 0 else 0
		return orientation
	def check_boundary(self, position):
		margin = const.sprite.SPRITE_SIZE / 2
		position = [max(i, margin) for i in position]
		position = [min(i, j - margin) for i, j in zip(position, const.screen.SCREEN_SIZE)]
		return position
	def check_speed(self, velocity, max_speed):
		if np.linalg.norm(velocity) > max_speed:
			velocity *= max_speed / np.linalg.norm(velocity)
		return velocity
	def update(self, steering, max_speed, time):
		self.position = self.check_boundary(self.position + self.velocity * time)
		self.velocity = self.check_speed(self.velocity + steering.linear * time, max_speed)
		#assign the the orientation of the velocity to the sprite
		self.orientation = self.velocity2orientation(self.velocity)
import numpy as np
from movement.steering import Steering
from math import isnan
class Kinematic(object):
	"""docstring for Kinematic"""
	def __init__(self):
		super().__init__()
		self.position = np.zeros([2,], float)
		self.orientation = float(0)
		self.velocity = np.zeros([2,], float)
		self.rotation = float(0)
	def update(self, steering, maxSpeed, time):
		self.position += self.velocity * time
		self.orientation += self.rotation * time
		self.velocity += steering.linear * time
		#self.orientation += steering.angular * time
		a = self.velocity / np.linalg.norm(self.velocity)
		a[1] = -a[1]
		b = [0, 1]
		c = np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b)) 
		if ~isnan(c):
			self.orientation = np.arccos(c)
		else:
			self.orientation = 0
		
		#self.orientation = np.arctan(self.velocity[0] / self.velocity[1])

		if np.linalg.norm(self.velocity) > maxSpeed:
			self.velocity /= np.linalg.norm(self.velocity) # nomalization
			self.velocity *= maxSpeed


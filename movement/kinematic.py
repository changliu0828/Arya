import numpy as np
from movement.steering import Steering
class Kinematic(object):
	"""docstring for Kinematic"""
	position = np.zeros([2, 1])
	orientation = float(0)
	velocity = np.zeros([2, 1])
	rotation = float(0)
	def __init__(self):
		super(Kinematic, self).__init__()
	def update(self, steering, maxSpeed, time):
		self.position += self.velocity * time
		self.orientation += self.rotation * time

		self.velocity += steering.linear * time
		self.orientation += steering.angular * time

		if np.linalg.norm(self.velocity) > maxSpeed:
			self.velocity /= np.linalg.norm(self.velocity) # nomalization
			self.velocity *= maxSpeed

if __name__ == "__main__":
	k = Kinematic()
	s = Steering()
	print(k.position, k.orientation, k.velocity, k.rotation)
	k.update(s, 100, 1)

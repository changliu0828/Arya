import numpy as np
from Static import Static
from Steering import Steering
maxSpeedmaxSpeed = 10
class Seek(object):
	"""docstring for Static"""
	character = Static()
	target = Static()
	def __init__(self):
		super(Seek, self).__init__()
	def getSteering(self, steering):
		steering.linear = self.target.position - self.character.position
		steering.linear /= np.linalg.norm(steering.linear)
		steering.linear *= maxSpeedmaxSpeed
		steering.angular = 0

if __name__ == "__main__":
	seek = Seek()
	steering = Steering()
	seek.getSteering(steering)
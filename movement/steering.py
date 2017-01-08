import numpy as np
class Steering(object):
	"""docstring for Steering"""
	def __init__(self):
		super().__init__()
		self.linear = np.zeros([2,])
		self.angular = float(0)

if __name__ == "__main__":
	s = Steering()
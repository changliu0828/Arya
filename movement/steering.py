import numpy as np
class Steering(object):
	"""docstring for Steering"""
	linear = np.zeros([2, 1]);
	angular = float(0)
	def __init__(self):
		super(Steering, self).__init__()
		

if __name__ == "__main__":
	s = Steering()
	print(s.linear, s.angular)
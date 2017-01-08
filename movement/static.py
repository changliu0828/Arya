import numpy as np
class Static(object):
	"""docstring for Static"""
	position = np.zeros([2, 1])
	orientation = float(0)
	def __init__(self):
		super(Static, self).__init__()

if __name__ == "__main__":
	s = Static()
	print(s.position, s.orientation)

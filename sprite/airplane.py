import sprite.asprite

class Airplane(sprite.asprite.ASprite):
	def __init__(self, color, pos):
		image_file = "Res/airplane.png"
		sprite.asprite.ASprite.__init__(self, image_file, color, pos)
	def update(self, direction):
		pass
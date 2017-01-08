import sprite.asprite

class Airplane(sprite.asprite.ASprite):
	def __init__(self, color, pos):
		image_file = "Res/airplane.jpg"
		super().__init__(image_file, color, pos)
	def update(self, key):
		super().update()
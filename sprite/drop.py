import sprite.asprite

class Drop(sprite.asprite.ASprite):
	def __init__(self, color, pos):
		image_file = "Res/drop.png"
		sprite.asprite.ASprite.__init__(self, image_file, color, pos)
	def update(self, direction):
		self.rect.move_ip(direction[0],direction[1])
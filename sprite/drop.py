import sprite.asprite
import sprite.update_decorator.key
import const.sprite

class Drop(sprite.asprite.ASprite):
	def __init__(self, color, pos):
		image_file = "Res/drop.png"
		super().__init__(image_file, color, pos)
	
	@sprite.update_decorator.key.arrow_move(const.sprite.MAX_VELOCITY_2)
	def update(self, key):
		super().update()
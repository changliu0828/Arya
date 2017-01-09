import sprite.asprite
import sprite.update_decorator.ai_movement
import const.sprite


class Airplane(sprite.asprite.ASprite):
	def __init__(self, color, pos):
		image_file = "Res/airplane.png"
		super().__init__(image_file, color, pos)

	@sprite.update_decorator.ai_movement.wandering(const.sprite.MAX_VELOCITY_2)
	def update(self):
		super().update()
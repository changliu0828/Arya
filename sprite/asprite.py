import pygame
from pygame.locals import *
import const.screen
import const.sprite
import movement.kinematic
import numpy as np

class ASprite(pygame.sprite.Sprite):
	# @param image_file
	# @param color
	# @param pos: position of the sprite on the screen. 
	# 	Top-left is (0,0), and Bottom-right is (1,1) 
		
	def __init__(self, image_file, color, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		shrink = const.sprite.SPRITE_SIZE / max(self.image.get_width(), self.image.get_height())
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * shrink), int(self.image.get_height() * shrink)))
		self.image.fill(color, None, BLEND_ADD)

		self.init_image = self.image
		
		self.rect = self.image.get_rect()
		self.rect.center = (pos[0] * const.screen.SCREEN_WIDTH , pos[1] * const.screen.SCREEN_HEIGHT)
		self.kinematic = movement.kinematic.Kinematic()
		self.kinematic.position = np.asarray(self.rect.center, float)
		self.steering = movement.steering.Steering()

	def update(self):
		#print("A", self.kinematic.orientation * 180 / np.pi)
		#self.image = pygame.transform.rotate(self.init_image, self.kinematic.orientation * 180 / np.pi)
		self.rect = self.image.get_rect()
		self.rect.center = self.kinematic.position
		pass
import pygame
from pygame.locals import *
from sys import exit
import const.screen
import const.color
from sprite.drop import Drop
from sprite.airplane import Airplane
import numpy

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode(const.screen.SCREEN_SIZE, 0, const.screen.SCREEN_DEPTH)
	clock = pygame.time.Clock()
	drop = Drop(const.color.RED, (0.5, 0.5))
	airplane = Airplane(const.color.BLACK, (0.3, 0.3))
	group = pygame.sprite.Group()
	group.add(drop)
	group.add(airplane)
	
	#main loop
	while True:
		event = pygame.event.poll()
		if event.type == QUIT:
			exit()
		key = pygame.key.get_pressed()

		collide = pygame.sprite.collide_rect(drop,airplane)

		group.update(key)
		screen.fill(const.color.WHITE)
		group.draw(screen)
		pygame.display.flip()
		clock.tick(const.screen.FRAME_RATE)
		
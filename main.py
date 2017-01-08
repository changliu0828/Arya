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
	screen = pygame.display.set_mode((const.screen.SCREEN_WIDTH, const.screen.SCREEN_HEIGHT), 0, const.screen.SCREEN_DEPTH)
	screen.fill(const.color.WHITE)
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
		
		direction = numpy.array([0, 0])
		if key[pygame.K_UP]:
			direction += [0, -1]
		if key[pygame.K_DOWN]:
			direction += [0, 1]
		if key[pygame.K_LEFT]:
			direction += [-1, 0]
		if key[pygame.K_RIGHT]:
			direction += [1, 0]

		group.update(direction)
		screen.fill(const.color.WHITE)
		group.draw(screen)
		pygame.display.flip()
		clock.tick(const.screen.FRAME_RATE)
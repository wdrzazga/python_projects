import pygame
import sys
from lib import Constants
from ball import Ball


pygame.init()

screen = pygame.display.set_mode(Constants.screen_size)

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

ball = Ball()

time = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(Constants.BLACK)

	clock.tick(60)
	# time = (pygame.time.get_ticks() - start_time) / 60

	time += 0.01
	ball.throw(100, 1, time)

	ball.draw(screen)

	pygame.display.flip()

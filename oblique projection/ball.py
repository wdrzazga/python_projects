import pygame
from lib import Constants
import math

class Ball:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.size = 5

	def throw(self, speed, angle, time):
		self.x = speed * time * math.cos(angle)
		self.y = speed * time * math.sin(angle) - 9.81 * time**2 // 2
		#self.y = Constants.screen_size[1] -y

		print(self.x, self.y)

	def draw(self, screen):
		pygame.draw.circle(screen, Constants.RED, (self.x, self.y), self.size)
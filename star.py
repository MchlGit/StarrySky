import pygame
from pygame.sprite import Sprite

class Start(Sprite): 
	def __init__(self, starry_night): 
		self.screen = starry_night.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()

		self.rect_x = self.rect.width
		self.rect_y = self.rect.height
		
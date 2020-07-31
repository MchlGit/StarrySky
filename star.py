import pygame
from pygame.sprite import Sprite

class Star(Sprite): 
	def __init__(self, starry_night): 

		super().__init__()
		self.screen = starry_night.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('images/star.bmp')
		self.twinkle = False
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# store star's exact horizonal position
		self.x = float(self.rect.x)
		
	def twinkle_star(self):
		self.twinkle = not self.twinkle
		if self.twinkle == True: 
			self.image = pygame.image.load('images/twinkle2.bmp')
		else: 
			self.image = pygame.image.load('images/star.bmp')

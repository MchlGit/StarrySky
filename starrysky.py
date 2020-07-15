import sys
import pygame 
from settings import Settings
from star import Star

class StarrySky: 
	def __init__(self): 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Starry Sky")
		self.stars = pygame.sprite.Group()
		self._create_stars()

	def run_game(self): 
		while True: 
			self._check_events()
			self._update_screen()

	def _check_events(self): 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit()


	def _update_screen(self): 
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)
		pygame.display.flip()

	def _create_stars(self): 
		star = Star(self)
		star_width, star_height = star.rect.size

		available_width = self.settings.screen_width - (2 * star_width)
		num_stars = available_width // (2* star_width)
		available_height = self.settings.screen_height - (2* star_height)
		num_rows = available_height // (2 * star_height)

		for row_number in range(num_rows): 
			for star_number in range(num_stars): 
				self._create_star(star_number, row_number)

	def _create_star(self, star_number, row_number): 
		new_star = Star(self)
		star_width, star_height = new_star.rect.size
		new_star.x = star_width + (2 * star_width * star_number)
		new_star.rect.x = int(new_star.x)
		new_star.rect.y = star_height + (2 * star_height * row_number)
		self.stars.add(new_star)

if __name__ == '__main__': 
	ss = StarrySky()
	ss.run_game()
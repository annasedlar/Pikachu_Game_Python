import pygame;
from pygame.sprite import Sprite; 

class Enemy(Sprite):
	def __init__(self, screen, game_settings):
		# this passes our stuff up to parent
		super(Enemy, self).__init__();
		self.image = pygame.image.load('team_rocket.png');
		self.image = pygame.transform.scale(self.image, (200,200)); 
		self.speed =2; 
		# find location and size of image that just loaded
		self.rect = self.image.get_rect(); 
		# find the location and size of screen
		self.screen_rect = screen.get_rect(); 
		# set up screen
		self.screen = screen;
		# set the center of the image
		self.rect.centery = self.screen_rect.centery;
		self.rect.right = self.screen_rect.right; 
	def draw_me(self):
		self.screen.blit(self.image, self.rect); 
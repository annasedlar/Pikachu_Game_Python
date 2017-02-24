import pygame;

# this will get the sprite class from pygame.sprite
# our here will be a sprite object
from pygame.sprite import Sprite; 

class Hero(Sprite):
	# initialize class properties
	def __init__(self, screen):
		super(Hero,self).__init__();
		self.image = pygame.image.load('pikachu.png');
		self.image = pygame.transform.scale(self.image, (100,100)); 
		self.screen = screen; 
		# create a rect prop that will be the dimensions and location of the image
		# it's availabe in get)rect because this is a pygame image
		# print self.image.get_rect(); 
		self.rect = self.image.get_rect(); 
		# now that we have the screen object from main, get the size of screen
		self.screen_rect = screen.get_rect();
		print self.screen_rect;
		# this will put the middle of the hero at the middle of the screen 
		self.rect.centery = self.screen_rect.centery;
		# this will put the left side of the hero at the left side of the screen
		self.rect.left = self.screen_rect.left;

	def draw_me(self): 
		# BLIT = Block Image Transfer - take pixels from image and replace part of your screen with them
		self.screen.blit(source = self.image, dest = self.rect)






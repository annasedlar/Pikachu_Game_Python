
# include pygame again. we have it because we pip installed it in terminal
import pygame;

# this will get the sprite class from pygame.sprite
# our here will be a sprite object - special objects in pygame that come with cool features
from pygame.sprite import Sprite; 

# create a class of hero, make it a subclass of Sprite
class Hero(Sprite):
	# initialize class properties.
	# classes have two parts: properties/data, methods. 
	def __init__(self, screen, image, settings):
		# bc this is a subclass, we need to call super so that the parent class gets the data
		super(Hero,self).__init__();
		self.image = pygame.image.load(image);
		self.image = pygame.transform.scale(self.image, (70,70)); 
		# add the screen to the object so we can reuse it as needed
		self.screen = screen; 
		# create a rect prop that will be the dimensions and location of the image (x, y)
		# it's availabe in get_rect because this is a pygame image
		# print self.image.get_rect(); 
		self.rect = self.image.get_rect(); 
		# now that we have the screen object from main, get the size of screen
		# ie. finding the location and size of our screen with get_rect()
		self.screen_rect = screen.get_rect();
		print self.screen_rect;
		# put the middle of the hero at the middle of the screen 
		self.rect.centery = self.screen_rect.centery;
		# put the left side of the hero at the left side of the screen
		self.rect.left = self.screen_rect.left;
		# set up movement booleans. All init @ false
		self.moving_right = False; 
		self.moving_left = False; 
		self.moving_up = False; 
		self.moving_down = False; 
		self.speed = settings.speed;

	def update_me(self): 
		# if user pushes left, move self.rect left etc... 
		if self.moving_right:
			self.rect.centerx +=10 * self.speed; 
		elif self.moving_left: 
			self.rect.centerx -=10 * self.speed; 
		elif self.moving_up:
			self.rect.centery -=10 * self.speed; 
		elif self.moving_down: 
			self.rect.centery +=10 * self.speed; 

	def draw_me(self): 
		# BLIT = Block Image Transfer - take pixels from image and replace part of your screen with them
		# first arg is what, second is where (just like reactDOM.render)
		self.screen.blit(source = self.image, dest = self.rect)



















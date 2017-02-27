import pygame; 
from pygame.sprite import Sprite; 


class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings, direction, bullet_type): 
		super(Bullet, self).__init__();
		# get screen so object can use it whenever needed
		self.screen = screen; 
		# self.rect = pygame.Rect();
		if bullet_type == "vertical":
			self.rect = pygame.Rect(0,0, game_settings.bullet_width, game_settings.bullet_height)
		elif bullet_type == "horizontal":
			self.rect = pygame.Rect(0,0, game_settings.bullet_height, game_settings.bullet_width)
		# create a bullet from scratch
		self.rect = pygame.Rect(0,0, game_settings.bullet_width, game_settings.bullet_height);
		# set the centerx of the bullet we just created to the centerx of the hero
		self.rect.centerx = hero.rect.centerx; 
		#set the top to the hero top
		# self.rect.top = hero.rect.top; 
		self.rect.centery = hero.rect.centery
		# set the color of the bullet from settings
		self.color = game_settings.bullet_color; 
		self.speed = game_settings.bullet_speed;
		# create an x and y property
		self.x = self.rect.x; 
		self.y = self.rect.y; 
		self.direction = direction;

	def draw_bullet(self):
		# drawrect takes 3 args: where(@what entity), what color, what
		pygame.draw.rect(self.screen, self.color, self.rect)

	def update(self): 
		if self.direction == 'right': 
		# change x and y accordingly based on self.speed
		# change y everything update runs
		# self.y -= self.speed; 
			self.x += self.speed
		if self.direction == 'up':
			self.y -= self.speed; 
		elif self.direction == 'left': 
			self.x -= self.speed; 
		elif self.direction == 'down': 
			self.x += self.speed; 

		# actually change the y coord of the bullet to be self.y
		self.rect.y = self.y
		self.rect.x = self.x


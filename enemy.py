import pygame;
from pygame.sprite import Sprite; 

class Enemy(Sprite):
	def __init__(self, screen, game_settings):
		# this passes our stuff up to parent
		super(Enemy, self).__init__();
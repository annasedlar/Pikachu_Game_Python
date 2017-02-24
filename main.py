import pygame;

import sys; 

from settings import Settings; 

# get our hero class
from hero import Hero; 

# initialize all of the pygame modules
pygame.init();

# put a message on the status bar so the player knows the name of the game
pygame.display.set_caption("Monster Attack");
 # create an object out of our settings class
game_settings = Settings(); 
screen = pygame.display.set_mode(game_settings.screen_size); 
hero = Hero(screen);


# this loop will run forever, while 1... 
while 1:
	for event in pygame.event.get(): 
		# this means the user quit by clicking on the red x
		if event.type == pygame.QUIT: 
			# stop the game, the user wants off
			sys.exit(); 
		# check for key press (any key)
		elif event.type == pygame.KEYDOWN:
			print event.key
			# user pressed RIGHT key
			if event.key == pygame.K_RIGHT:
				print "pressed right";
				hero.moving_right = True;
			elif event.key == pygame.K_LEFT:
				print "pressed left"
				hero.moving_left = True; 
			elif event.key == pygame.K_UP:
				print "pressed up"
				hero.moving_up = True; 
			elif event.key == pygame.K_DOWN:
				print "pressed down"
				hero.moving_down = True; 
		elif event.type == pygame.KEYUP:
			print event.key
			# user pressed RIGHT key
			if event.key == pygame.K_RIGHT:
				print "pressed right";
				hero.moving_right = False;
			elif event.key == pygame.K_LEFT:
				print "pressed left"
				hero.moving_left = False; 
			elif event.key == pygame.K_UP:
				print "pressed up"
				hero.moving_up = False; 
			elif event.key == pygame.K_DOWN:
				print "pressed down"
				hero.moving_down = False; 


		# put our BG color as the fill color of game
		screen.fill(game_settings.bg_color);
		# allow movement
		hero.update_me();

		hero.draw_me(); 
		# flip the screen  = wipe it out
		pygame.display.flip(); 



























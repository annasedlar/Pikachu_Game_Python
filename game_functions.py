# all game functions

import pygame;

# to halt our program
import sys; 

from hero import Hero; 


def check_events(hero):
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






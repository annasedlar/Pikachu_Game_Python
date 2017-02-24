# all game functions

import pygame;

# to halt our program
import sys; 

from hero import Hero; 

import vlc;

def check_events(hero, start_button, game_settings):
	for event in pygame.event.get(): 
			# this means the user quit by clicking on the red x
			if event.type == pygame.QUIT: 
				# stop the game, the user wants off
				sys.exit(); 
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos();
				# print mouse_x, mouse_y; 
				# collidepoint is non group way
				if start_button.rect.collidepoint(mouse_x, mouse_y):
					game_settings.game_active = True; 
					bg_music = vlc.MediaPlayer("pika_happy.mp3"); 
					bg_music.play()
					# bg_music = pygame.mixer.Sound('faf.wav');
					# bg_music.play();
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






import pygame;

from settings import Settings; 

# get our hero class
from hero import Hero; 

from game_functions import check_events

# from pygame get the sprite stuffa nd groupcollide to handle collision
from pygame.sprite import Group, groupcollide

from enemy import Enemy; 
# initialize all of the pygame modules
pygame.init();

# put a message on the status bar so the player knows the name of the game
pygame.display.set_caption("Monster Attack");
 # create an object out of our settings class
game_settings = Settings(); 
screen = pygame.display.set_mode(game_settings.screen_size); 

hero = Hero(screen, game_settings);

enemies = Group(); 
enemies.add(Enemy(screen, game_settings));


# this loop will run forever, while 1... 
while 1:
	# run our check_events here
	check_events(hero);

	# put our BG color as the fill color of game
	screen.fill(game_settings.bg_color);
	# allow movement
	hero.update_me();

	hero.draw_me(); 

	# loop because enemy is in Group()
	for enemy in enemies.sprites():
		enemy.draw_me();

	# flip the screen  = wipe it out
	pygame.display.flip(); 



























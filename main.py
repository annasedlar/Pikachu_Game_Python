import pygame;

from settings import Settings; 

# get our hero class
from hero import Hero; 

from game_functions import check_events

# from pygame get the sprite stuffa nd groupcollide to handle collision
from pygame.sprite import Group, groupcollide

from enemy import Enemy; 

from start_button import Start_Button;

# initialize all of the pygame modules
pygame.init();

# put a message on the status bar so the player knows the name of the game
pygame.display.set_caption("Monster Attack");
 # create an object out of our settings class
game_settings = Settings(); 
screen = pygame.display.set_mode(game_settings.screen_size); 

start_button = Start_Button(screen); 

# make a group for the hero to belong to so we an use groupcollide
hero_group = Group(); 
hero = Hero(screen, game_settings);
# put hero in group
hero_group.add(hero)

enemies = Group(); 
enemies.add(Enemy(screen, game_settings));

# this loop will run forever, while 1... 
while 1:
	# run our check_events here
	check_events(hero, start_button, game_settings);

	# put our BG color as the fill color of game
	screen.fill(game_settings.bg_color);

	for hero in hero_group.sprites():
		if game_settings.game_active:
			# allow movement
			hero.update_me();
		hero.draw_me(); 

	# loop because enemy is in Group()
	for enemy in enemies.sprites():
		if game_settings.game_active:
		# pass the hero as a param so it knows who to follow
			enemy.update_me(hero); 
		enemy.draw_me();
	hero_died = groupcollide(hero_group, enemies, True, True);

	if hero_died: 
		print "*************************************"
		print "*************************************"
		print "************YOU LOST!****************"
		print "*************************************"
		print "*************************************"
		game_settings.game_active == False; 
	if game_settings.game_active == False:
		start_button.draw_button();
	
	# start_button.draw_button(); 

	# flip the screen  = wipe it out
	pygame.display.flip(); 



























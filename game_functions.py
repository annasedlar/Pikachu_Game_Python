# all game functions

import pygame;

# to halt our program
import sys; 

from hero import Hero; 

def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pygame.mixer.music.set_volume(volume)
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)
# pick a MP3 music file you have in the working folder
# otherwise give the full file path
# (try other sound file formats too)
music_file = "pika_happy.mp3"
# optional volume 0 to 1.0
volume = 0.8


def check_events(hero, start_button, game_settings):
	for event in pygame.event.get(): 
			# this means the user quit by clicking on the red x
			# we want to patch into certain events, like click/keypress/quit... 
			# check to see if the occred event is the quit event
			if event.type == pygame.QUIT: 
				# stop the game, the user wants off
				sys.exit(); 
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos();
				# print mouse_x, mouse_y; 
				# collidepoint is non group way
				if start_button.rect.collidepoint(mouse_x, mouse_y):
					game_settings.game_active = True; 
					# bg_music = pygame.mixer.Sound('pika_happy.mp3');
					# bg_music.play();
					play_music(music_file, volume)
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






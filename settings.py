# a place to hold all of our game settings


class Settings(object): 
	def __init__(self): 
		# will expect a tuple that is the expected screen size
		self.screen_size = (800,800)
		# make a background color (take RGB values - (0-255 for R, G, B): 
		self.bg_color = (82, 111, 53);
		self.speed = 2; 
		self.game_active = False; 

		self.bullet_width = 20; 
		self.bullet_height = 3; 
		self.bullet_speed = 4;
		self.bullet_color = (0,0,0);
		self.timer = 0;



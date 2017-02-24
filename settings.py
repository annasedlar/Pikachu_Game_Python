# a place to hold all of our game settings


class Settings(object): 
	def __init__(self): 
		# will expect a tuple that is the expected screen size
		self.screen_size = (600,600)
		# make a background color (take RGB values - (0-255 for R, G, B): 
		self.bg_color = (82, 111, 53);
		self.speed = 1; 
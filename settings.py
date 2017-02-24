# a place to hold all of our game settings

# BLIT = Block Image Transfer - take pixels from image and replace part of your screen with them

class Settings(object): 
	def __init__(self): 
		# will expect a tuple that is the expected screen size
		self.screen_size = (600,600)
		# make a background color (take RGB values - (0-255 for R, G, B): 
		self.bg_color = (82, 111, 53);
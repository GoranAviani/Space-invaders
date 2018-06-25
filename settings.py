
class Settings():

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
       # Light gray
        self.bg_color = (0, 0, 0)

        #Ship settings
        #On mowing ship position will be changed (from 1px originally) 1.5px in any direction
        self.ship_speed_factor = 1.5

        #Bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
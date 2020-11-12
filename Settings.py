class Setting(object):
    def __init__(self):
        #Screen setting
        self.width = 1200
        self.height = 600
        self.backgr_col = (255,255,255)
        #Ship setting
        self.ship_speed = 1.2
        self.ship_limit = 3
        #Bullets setting
        self.bullet_speed = 1.0
        self.bullet_width = 3.0
        self.bullet_height = 15
        self.bullet_col = (60,60,60)
        self.bullets_allowed = 5
        #Aliens setting
        self.alien_speed = 0.3
        self.fleet_drop_speed =50
        self.fleet_direction = 1
        #Rain setting
        self.rain_speed = 0.1
        self.score_scale = 1.0005
        # Speeding up the game
        self.speedup_scale = 1.1
        self.init_dynamic_settings()
        self.alien_points = 20

    def init_dynamic_settings(self):
        self.ship_speed = 1.3
        self.bullet_speed = 1.0
        self.alien_speed = 0.25
        self.level = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= int(self.alien_points*self.score_scale)
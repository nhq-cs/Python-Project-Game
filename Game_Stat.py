class Game_Stats(object):
    def __init__(self,game):
        self.setting = game.setting
        self.game_active = False
        self.score = 0
        self.reset_stats()
        self.high_score = 0
        self.level = 1
    def reset_stats(self):
        self.ship_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    "A class to manage bullets fired from the ship"
    def __init__(self,game):
        "Creating bullets at the ship's postition"
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.color = self.setting.bullet_col
        "Creating bullets at (0,0)"
        self.rect = pygame.Rect(0,0,self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
    def update(self):
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y
    def bullet_draw(self):
            pygame.draw.rect(self.screen, self.color, self.rect)
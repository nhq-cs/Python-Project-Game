import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        #Load image
        self.image = pygame.image.load('Image/Aliens.png')
        self.rect = self.image.get_rect()
         #Create a new one
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
         #Store
        self.x = float(self.rect.x)
    def update(self):
        """Move aliens to the right"""
        self.x += self.setting.alien_speed * self.setting.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if aliens are at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

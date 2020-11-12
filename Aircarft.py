import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('Image/rsz_rsz_1rsz_rocket.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rightFlag = False
        self.leftFlag = False
        self.upFlag = False
        self.downFlag = False
        self.setting = game.setting
        self.x = float(self.rect.x)
    def DrawMe(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.rightFlag == True:
            self.rect.x +=1
            if self.rightFlag and self.rect.right < self.screen_rect.right:
                self.x += self.setting.ship_speed
        if self.leftFlag == True:
            self.rect.x -= 1
            if self.leftFlag and self.rect.left > 0:
                self.x -= self.setting.ship_speed
        if self.upFlag == True:
            self.rect.y -=1
            #if self.upFlag and self.rect.up < self.rect.up:
             #   self.y += self.setting.ship_speed
        if self.downFlag == True:
            self.rect.y +=1
            #if self.downFlag and self.rect.down > 0:
                #self.y -= self.setting.ship_speed
        self.rect.x = self.x
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

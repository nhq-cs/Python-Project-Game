"""
Author: @Quang Nguyen
Email: quang.nguyencse272.hcmut.edu.vn

"""
import sys
from time import sleep
import pygame
from Settings import Setting
from Aircarft import Ship
from Bullet import Bullet
from Aliens import Alien
from Game_Stat import Game_Stats
from Button import button
from Scoreboard import scoreboard
class Conquer(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Conquer')
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.width, self.setting.height))
        self.play_button = button(self,'Play Game')
        self.stats = Game_Stats(self)
        self.sb = scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()
        self.Fleet()

    def run(self):
        while True:
            self.check_event()
            if self.stats.game_active:
                self.ship.update()
                self.bullets_update()

                self.update_alien()
            self.update_screen()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keyDown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyUp(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_play_button(self, mouse_pos):
        button_clicked =  self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
                self.setting.init_dynamic_settings()
                pygame.mouse.set_visible(False)
                self.stats.reset_stats()
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_ships()
                self.stats.game_active = True
                #Get rid of remaining all aliens and bullets
                self.aliens.empty()
                self.bullets.empty()
                #Creating a new fleet and ship
                self.Fleet()
                self.ship.center_ship()

    def check_keyDown(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.rightFlag = True
            # The Rocket will move to the rightw
        elif event.key == pygame.K_LEFT:
            self.ship.leftFlag = True
        elif event.key == pygame.K_UP:
            self.ship.upFlag = True
        elif event.key == pygame.K_DOWN:
            self.ship.downFlag = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_p:
            self.stats.game_active = True
        elif event.key == pygame.K_ESCAPE:
            self.stats.game_active = False

    def check_keyUp(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.rightFlag = False
        elif event.key == pygame.K_LEFT:
            self.ship.leftFlag = False
        elif event.key == pygame.K_UP:
            self.ship.upFlag = False
        elif event.key == pygame.K_DOWN:
            self.ship.downFlag = False

    def update_screen(self):
        self.screen.fill(self.setting.backgr_col)
        self.ship.DrawMe()
        self.bullets.update()
        for bullet in self.bullets.sprites():
            bullet.bullet_draw()
        self.aliens.draw(self.screen)
        self.sb.showsocre()
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def fire_bullet(self):
        if len(self.bullets) < self.setting.bullets_allowed:
            new = Bullet(self)
            self.bullets.add(new)

    def bullets_update(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_collision()
    # Check whether aliens collide the bullets
    def check_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.setting.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self.Fleet()
            self.setting.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
    def Fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        ship_height = self.ship.rect.height
        valid_spaceY = self.setting.height - 3*alien_height - ship_height
        number_rows = valid_spaceY // (2*alien_height)
        valid_spaceX = self.setting.width - (2*alien_width)
        number_aliens = valid_spaceX // (2*alien_width)
        for rows in range(number_rows):
            for alien_number in range(number_aliens):
                self.create_aliens(alien_number,rows)

    def check_Fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_Fleet_direction()
                break

    def change_Fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def create_aliens(self, alien_number, rows):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.heigt = alien.rect.height
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height * rows
        self.aliens.add(alien)


    def update_alien(self):
        self.check_Fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        self.check_alien_bottom()

    def ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -=1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()

            self.Fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break


if __name__ == '__main__':
    game = Conquer()
    game.run()

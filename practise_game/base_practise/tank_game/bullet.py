# 子弹类
import pygame

from practise_game.base_practise.tank_game.base_item import BaseItem



class Bullet(BaseItem):
    def __init__(self,tank):
        self.image = pygame.image.load('tank/tankA.png')
        self.direction = tank.direction
        self.rect = self.image.get_rect()
        self.rect.x = tank.rect.x
        self.rect.y = tank.rect.y-50
    def dispaly(self):

        screen.blit(self.image,(self.rect.x,self.rect.y))


# 树莓,随机生成的方块
import random


import pygame

from practise_game.base_practise.gluttonous_snake.CONSTANT import SCRREN_WIDTH,SCRREN_HEIGHT
from practise_game.base_practise.gluttonous_snake.base_item import BaseItem

red = (255, 0, 0)

class Rasspberry(BaseItem):

    def __init__(self):
        super().__init__()
        self.width = 5
        self.height = self.width
        self.image = pygame.Surface((self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCRREN_WIDTH)
        self.rect.y = random.randint(0, SCRREN_HEIGHT)
        self.image.fill(red)
        self.is_alive = True

    def update(self):
        self.rect.x = random.randint(0, SCRREN_WIDTH)
        self.rect.y = random.randint(0, SCRREN_HEIGHT)

    def get_eaten(self):
        pass
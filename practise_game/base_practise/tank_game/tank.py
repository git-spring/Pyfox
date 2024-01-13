# 坦克类

import pygame

from practise_game.base_practise.tank_game.base_item import BaseItem


class Tank(BaseItem):
    def __init__(self, tank_pos):
        super().__init__()
        self.images = {'W':pygame.image.load('tank/tankW.png'),
                      'S':pygame.image.load('tank/tankS.png'),
                      'A':pygame.image.load('tank/tankA.png'),
                      'D':pygame.image.load('tank/tankD.png')}
        self.direction = 'W'  # 坦克方向
        self.tank = self.images[self.direction]  # 根据方向获取图片
        self.rect = self.tank.get_rect()  # 图形区域
        self.rect.x = tank_pos[0]
        self.rect.y = tank_pos[1]
        self.speed = 10  # 坦克速度
        self.alive = True  # 坦克是否存活
        self.prev_x = self.rect.x  # 之前位置的X坐标
        self.prev_y = self.rect.y  # 之前位置的Y坐标

    def tank_move(self):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        if self.direction == 'W':
            if self.rect.y > 0:
                self.rect.y -= self.speed
        elif self.direction == 'S':
            if self.rect.y + self.rect.height < SCREEN_HEIGHT:
                self.rect.y += self.speed
        elif self.direction == 'A':
            if self.rect.x > 0:
                self.rect.x -= self.speed
        elif self.direction == 'D':
            if self.rect.x + self.rect.width < SCREEN_WIDTH:
                self.rect.x += self.speed

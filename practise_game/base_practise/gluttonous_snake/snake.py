# 玩家控制的蛇
import random

import pygame

from practise_game.base_practise.gluttonous_snake.base_item import BaseItem

red = (255, 0, 0)
yello = (255, 255, 0)



class Snake(BaseItem):
    def __init__(self, screen):
        super().__init__()
        self.color = yello
        self.width = 5
        self.height = self.width
        self.speed = 3
        self.direction = 'W'  # 方向
        self.head_x = random.randint(0, 100)  # 随机坐标 X
        self.head_y = random.randint(screen.get_size()[1]-100, screen.get_size()[1])  # 随机坐标 Y
        self.tail_x = self.head_x
        self.tail_y = self.head_y
        self.prev_x = self.head_x
        self.prev_y = self.head_y
        self.snake = pygame.draw.rect(screen, self.color, (self.head_x, self.head_y, self.width, self.width))
        self.is_alive = True

    def move(self):

        if self.direction == 'W':
            self.head_y = self.head_y - self.speed
        elif self.direction == 'S':
            self.head_y = self.head_y + self.speed
        elif self.direction == 'A':
           self.head_x = self.head_x - self.speed
        elif self.direction == 'D':
            self.head_x = self.head_x + self.speed

    def eat_raspberry(self):
        pass

# 方块跟随鼠标移动
from time import sleep

import pygame
import sys
from pygame.time import delay

# 方块类
class Block:
    def __init__(self,color,rect):
        self.color = color
        self.rect = rect
        self.block_x = rect[0]
        self.block_y = rect[1]
        self.block_w = rect[2]
        self.block_h = rect[3]
        pygame.draw.rect(screen, self.color, self.rect)

    def block_move(self,speed):
        pygame.draw.rect(screen, bg_color, (self.block_x,self.block_y,self.block_w,self.block_h)) # 先把之前的覆盖成背景色

        # 检测是否超出边界
        if 0 < self.block_x < screen.get_size()[0]-self.block_w:
            print(111)
            print(self.block_x)
            self.block_x = self.block_x + speed
        elif self.block_x <= 0:
            self.block_x = 0.01
        elif self.block_x >= screen.get_size()[0]-self.block_w:
            self.block_x = screen.get_size()[0]-self.block_w - 0.01
        pygame.draw.rect(screen, self.color, (self.block_x,self.block_y,self.block_w,self.block_h)) # 重画方块








pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 400))  # 设置窗口大小
pygame.display.set_caption('the window')  # 设置窗口名称

rx, ry, rw, rh = (30, 350, 100, 10)  # 方块的初始坐标,宽高
red = (255, 0, 0)
bg_color = (0,0,0)
block = Block( red, (30, 350, 100, 10))



move = False  # 是否可以移动
prev_pos = (0,0) # 鼠标上次的位置
pygame.display.flip()  # 第一次更新窗口

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            curr_pos = event.pos  # 鼠标当前位置
            dx = curr_pos[0] - prev_pos[0] # 水平方向上的移动
            dy = curr_pos[1] - prev_pos[1] # 垂直方向上的移动

            if curr_pos[1] >= block.block_y :
                move = True
            if move :
                block.block_move(dx)
                move = False
            prev_pos = curr_pos



    # clock = pygame.time.Clock()
    # time_passed = clock.tick(30)  # 刷新帧率
    pygame.display.update()  #

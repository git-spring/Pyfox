# 加载图片
from random import random

import pygame
import sys

from pygame.time import delay

pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 400))  # 设置窗口大小
pygame.display.set_caption('load image')  # 设置窗口名称

white = 255, 255, 255

screen.fill(white)

image = pygame.image.load('../../pig.png')  # 加载图片
# 1
image1 = pygame.transform.scale(image, (100, 100))  # 缩放图片(目标,(宽,高))
screen.blit(image1, (0, 0))  # 显示图片(目标,(目标位置))

# 2
image2 = pygame.transform.rotate(image1, 40)   # 旋转图片
screen.blit(image2, (100, 100))

# 3
image3 = pygame.transform.rotozoom(image, 45, 0.1)  # 旋转和缩放(目标,旋转角度,缩放比例)
screen.blit(image3, (50, 50))

image4 = pygame.transform.rotozoom(image, 180, 0.1)
screen.blit(image4, (screen.get_size()[0] - image3.get_size()[0], screen.get_size()[1] - image3.get_size()[1]))

pygame.display.flip()  # 第一次更新窗口

radius = 0 # 初始旋转角度

a=[10,10]

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()

    # 图片持续旋转
    radius += 1
    image5 = pygame.transform.rotozoom(image, radius, 0.1)
    screen.blit(image5, (300, 200))
    delay(20)

    pygame.display.update()  #

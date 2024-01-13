# 键盘事件


import pygame
import sys

pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 400))  # 设置窗口大小
pygame.display.set_caption('the window')  # 设置窗口名称
pygame.display.flip()  # 第一次更新窗口

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event.key, '对应的', chr(event.key), end=' ') # 键的编码和对应的键
            print('按键被按下')

        if event.type == pygame.KEYUP:
            print(event.key, '对应的', chr(event.key), end=' ')
            print('按键弹起')

    pygame.display.update()  #

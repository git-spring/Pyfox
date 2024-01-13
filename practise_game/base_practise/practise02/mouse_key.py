# 鼠标和键盘
# 在鼠标点击的位置显示一个矩形,并在其中输入文字,非输入法
from random import  randint

import pygame
import sys

pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 400))  # 设置窗口大小
pygame.display.set_caption('the window')  # 设置窗口名称
pygame.display.flip()  # 第一次更新窗口


WINDOW_WIDTH = screen.get_size()[0]
WINDOW_HEIGHT = screen.get_size()[1]
red = (255, 0, 0)
x, y = 0, 0 # 初始位置
interval = 20 # 每次输入文字的间隔
cursor_pos = [0,0]  # 当前光标位置



while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN :
            x,y = event.pos
            pygame.draw.rect(screen, red,(x,y,300,40),2)
            cursor_pos = [x,y]
            pygame.draw.rect(screen, (0, 0, 0), (WINDOW_WIDTH-150,WINDOW_HEIGHT-40, WINDOW_WIDTH,WINDOW_HEIGHT))

        if event.type == pygame.KEYDOWN:
            font = pygame.font.Font('../ttf/FZFSJW.TTF', 30)
            letter = chr(event.key)
            text = font.render(letter, True, (255, 255, 255))
            cursor_pos = [cursor_pos[0]+20,y]
            if cursor_pos[0] > x+280:  # 提示无法输入
                random_color = (randint(0, 255), randint(0, 255), randint(0, 255))  # 随机颜色
                notice = font.render('无法再输入', True, random_color)
                notice = pygame.transform.rotozoom(notice,0,1) # 文字缩放
                screen.blit(notice,(WINDOW_WIDTH-150,WINDOW_HEIGHT-40))
            else :
                screen.blit(text, (cursor_pos[0], y))  # 显示输入的文字
            print(letter)

    pygame.display.update()  #

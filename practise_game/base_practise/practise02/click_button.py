# 点击按钮

import pygame
import sys

pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 400))  # 设置窗口大小
pygame.display.set_caption('the window')  # 设置窗口名称

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

screen.fill(white)

cx, cy, cw, ch = 100, 100, 80, 30     # confirm_button 确认按钮 位置和宽高
cx1, cy1, cw1, ch1 = 100, 160, cw, ch  # cancle_button  取消按钮 位置和宽高

pygame.draw.rect(screen, red, (cx, cy, cw, ch))
font = pygame.font.Font('../ttf/FZQTJW.TTF', ch )
text = font.render('确定', True, white)
tw, th = text.get_size()
screen.blit(text, (cx + cw / 2 - tw / 2, cy + ch / 2 - th / 2)) # 显示按钮文字,文字居中

pygame.draw.rect(screen, green, (cx1, cy1, cw1, ch1))
text1 = font.render('取消', True, white)
tw1, th1 = text1.get_size()
screen.blit(text1, (cx1 + cw1 / 2 - tw1 / 2, cy1 + ch1 / 2 - th1 / 2)) # 显示按钮文字,文字居中

pygame.display.flip()  # 第一次更新窗口

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if event.button == 1:  # 点击左键才有效
                if mouse_x > cx and mouse_x < cx + cw and mouse_y > cy and mouse_y < cy + ch: # 点击确认按钮
                    pygame.draw.rect(screen, (200, 200, 200), (cx, cy, cw, ch))
                    screen.blit(text, (cx + cw / 2 - tw / 2, cy + ch / 2 - th / 2))
                    pygame.display.update()
                if mouse_x > cx1 and mouse_x < cx1 + cw and mouse_y > cy1 and mouse_y < cy1 + ch: # 点击取消按钮
                    pygame.draw.rect(screen, (200, 200, 200), (cx1, cy1, cw1, ch1))
                    screen.blit(text1, (cx1 + cw1 / 2 - tw1 / 2, cy1 + ch1 / 2 - th1 / 2))
                    pygame.display.update()

        if event.type == pygame.MOUSEBUTTONUP: # 鼠标弹起
            if event.button == 1:  # 左键才有效
                if mouse_x > cx and mouse_x < cx + cw and mouse_y > cy and mouse_y < cy + ch:
                    pygame.draw.rect(screen, red, (cx, cy, cw, ch))
                    screen.blit(text, (cx + cw / 2 - tw / 2, cy + ch / 2 - th / 2))
                    pygame.display.update()
                if mouse_x > cx1 and mouse_x < cx1 + cw and mouse_y > cy1 and mouse_y < cy1 + ch:
                    pygame.draw.rect(screen, green, (cx1, cy1, cw1, ch1))
                    screen.blit(text1, (cx1 + cw1 / 2 - tw1 / 2, cy1 + ch1 / 2 - th1 / 2))
                    pygame.display.update()
                    print(222)
    pygame.display.update()  #

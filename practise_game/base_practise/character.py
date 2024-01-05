# 显示文字


import pygame
import sys

from pygame.time import delay

pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 400))  # 设置窗口大小
pygame.display.set_caption('load image')  # 设置窗口名称

# screen.fill((255,255,255)) # 填充窗口颜色,默认黑色

# 显示文字
# 创建字体文件对象
# font = pygame.sysfont.Font()  # 系统字体
font = pygame.font.Font('./ttf/FZQTJW.TTF', 50)
text = font.render('一行汉字', True, (255, 255, 255), (155, 125, 0))  # (文字内容,抗锯齿,文字颜色,背景颜色)
screen.blit(text, (0, 0))  # 显示文字 (文字内容,(位置))

# 文字缩放
text2 = pygame.transform.scale(text, (100, 50))
screen.blit(text2, (0, 100))

# 文字缩放和旋转
text3 = pygame.transform.rotozoom(text, 90, 0.5)
screen.blit(text3, (0, 200))

pygame.display.flip()  # 第一次更新窗口


while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()

    pygame.display.update()  #

# 绘制简单图形


import pygame
import sys
from math import pi

pygame.init()  # 初始化
screen = pygame.display.set_mode((700, 500))  # 设置窗口大小
pygame.display.set_caption('simpe graphics')  # 设置窗口名称

# 直线
pygame.draw.line(screen, (255, 0, 0), (0, 30), (200, 30), 2)

# 多条线段
points = [(50, 50), (80, 70), (110, 170), (150, 150), (160, 200)]
pygame.draw.lines(screen, (255, 0, 0), True, points)

# 五角星
# todo : 多条线段画出五角星


# 矩形
pygame.draw.rect(screen, (0, 0, 255), (0, 220, 100, 50), 2)  # 不填充
pygame.draw.rect(screen, (0, 255, 255), (0, 280, 100, 50))  # 填充

# 圆⚪
pygame.draw.circle(screen, (255, 0, 0), (100, 300), 50)

# 椭圆
pygame.draw.ellipse(screen, (255, 0, 0), (50, 350, 150, 80))

# 三角形
pygame.draw.polygon(screen, (156, 245, 122), ((20, 100), (70, 100), (40, 130)), 3)

# 圆弧
pygame.draw.arc(screen, (156, 245, 122), (50, 350, 150, 80), 0, pi / 3, 2)

pygame.display.flip()  # 刷新窗口

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()

    pygame.display.update()  #

# 鼠标事件


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

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)  # 检测是鼠标上的哪个键
            print('鼠标按下')
        if event.type == pygame.MOUSEBUTTONUP:
            print('鼠标弹起')
        if event.type == pygame.MOUSEWHEEL:
            print('鼠标滚轮在滑动')
        if event.type == pygame.MOUSEMOTION:
            print('鼠标移动')
            print('当前位置:', event.pos)  # 鼠标位置
    pygame.display.update()  #

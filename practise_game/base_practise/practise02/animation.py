# 简单动画


import pygame
import sys

pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 400))  # 设置窗口大小
pygame.display.set_caption('the window')      # 设置窗口名称
clock = pygame.time.Clock()
pygame.display.flip()  # 第一次更新窗口

# 五角星
def pentagram():
    pass


ball = pygame.image.load('ball.png')
def move():
    ballrect = ball.get_rect()
    clock = pygame.time.Clock()


WINDOW_W, WINDOW_H = screen.get_size()[0], screen.get_size()[1]  # 窗体尺寸
FPS = 50  # 帧率，即每秒刷新多少次
g = 9.8 * 100  # 重力加速度（我们用的单位是像素每二次方秒）
x, y = 30, 10   # 球的坐标
vx, vy = 0, 0  # 球在x,y方向上的速度

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():   # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()
    # 小球下一时刻的速度、位置计算
    vy += g * 1 / FPS
    vx += 5/FPS
    x += vx * 1 / FPS
    y += vy * 1 / FPS
    if y >= WINDOW_H - 10:
        # 到达地面则是其竖直速度反向
        vy = -vy

    # 将背景图画上去(0,0,0)为RGB颜色
    screen.fill((0, 0, 0))
    # 根据球的坐标画圆
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 10)
    time_passed = clock.tick(FPS)
    pygame.display.update()  #



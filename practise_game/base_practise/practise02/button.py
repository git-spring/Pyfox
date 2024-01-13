# 按钮类封装
import pygame


class Button:


    def __init__(self, button_text, button_args, bg_color, text_color, text_size=20):
        """
        :param button_text:  按钮文字
        :param button_args: 按钮坐标,宽高
        :param bg_color:  背景颜色
        :param text_color:  按钮文字颜色
        """
        self.button_text = button_text
        self.button_args=button_args
        self.bg_color = bg_color
        self.text_color = text_color
        self.text_size = text_size


    def create(self):
        cx, cy, cw, ch = self.button_args  # 按钮的坐标,宽高
        back_color = (self.bg_color[0], self.bg_color[1], self.bg_color[2])
        text_color = (self.text_color[0], self.text_color[1], self.text_color[2])
        pygame.draw.rect(screen, back_color, (cx, cy, cw, ch))
        if self.text_size > ch : # 控制按钮文字大小
            self.text_size = ch
        elif self.text_size <15 :
            self.text_size = 15
        font = pygame.font.Font('../ttf/FZFSJW.TTF', self.text_size)
        text = font.render(self.button_text, True, text_color)
        tw, th = text.get_size()
        screen.blit(text, (cx + cw / 2 - tw / 2, cy + ch / 2 - th / 2))
        self.tw=tw
        self.th = th
        self.text = text

    def mouse_down(self):
        """
        鼠标点击时的动作
        :return:
        """
        cx, cy, cw, ch = self.button_args
        tw, th = self.tw,self.th
        text = self.text

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if event.button == 1:  # 点击左键才有效
                if mouse_x > cx and mouse_x < cx + cw and mouse_y > cy and mouse_y < cy + ch:
                    pygame.draw.rect(screen, (200, 200, 200), (cx, cy, cw, ch))
                    screen.blit(text, (cx + cw / 2 - tw / 2, cy + ch / 2 - th / 2))
                    print(111)
                    pygame.display.update()


    def mouse_up(self):
        """
        鼠标弹起时的动作
        :return:
        """
        cx, cy, cw, ch = self.button_args
        tw, th = self.tw,self.th
        text = self.text

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = event.pos
            if event.button == 1:  # 点击左键才有效
                if mouse_x > cx and mouse_x < cx + cw and mouse_y > cy and mouse_y < cy + ch:
                    pygame.draw.rect(screen, (255, 0, 0), (cx, cy, cw, ch))
                    screen.blit(text, (cx + cw / 2 - tw / 2, cy + ch / 2 - th / 2))
                    pygame.display.update()

import pygame
import sys

pygame.init()  # 初始化
screen = pygame.display.set_mode((600, 400))  # 设置窗口大小
pygame.display.set_caption('the window')  # 设置窗口名称


# button = Button('开始',  (200, 200, 80, 30),(255,0,0),(255, 255, 255))
# button = Button()
button = Button('开始',  (200, 200, 80, 30),(255,0,0),(255, 255, 255),50)
button.create()

button1 = Button('取消',  (200, 300, 80, 30),(0,255,0),(255, 255, 255),50)
button1.create()
pygame.display.flip()  # 第一次更新窗口

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()
        button.mouse_down()
        button.mouse_up()
    pygame.display.update()  #

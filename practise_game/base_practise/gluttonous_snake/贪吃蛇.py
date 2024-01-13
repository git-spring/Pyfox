# 贪吃蛇


import pygame
import sys

from pygame.time import delay

from practise_game.base_practise.gluttonous_snake.raspberry import Rasspberry
from practise_game.base_practise.gluttonous_snake.snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BG_COLOR = pygame.Color(0, 0, 0)


rass_group = pygame.sprite.Group()
rass = Rasspberry()


class MainGame:

    screen = None


    def start_game(self):
        pygame.init()  # 初始化
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 设置窗口大小
        pygame.display.set_caption('the window')  # 设置窗口名称
        snake = Snake(screen)

        pygame.display.flip()  # 第一次更新窗口

        while True:  # 死循环确保窗口一直显示
            screen.fill(BG_COLOR)
            for event in pygame.event.get():  # 遍历所有事件
                if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                    pygame.quit()
                    sys.exit()
                print(event.type)
                if event.type == pygame.KEYDOWN:
                    print(str.upper(chr(event.key)))
                    snake.direction = str.upper(chr(event.key))
            snake.move()

            pygame.draw.rect(screen,snake.color,(snake.head_x,snake.head_y,snake.width,snake.height))


            rass_group.add(rass)
            rass_group.draw(screen)
            rass_group.update()
            delay(500)
            # clock = pygame.time.Clock()
            # time_passed = clock.tick(30)  # 刷新帧率
            pygame.display.update()  #


if __name__ == '__main__':
    MainGame().start_game()
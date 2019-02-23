#!python3
# -*- coding: UTF-8 -*-
# 版权所有 © 2019 向昕哲
# 本程序为自由软件，在自由软件联盟发布的GNU通用公共许可协议的约束下，你可以对其进行再发布及修改。协议版本为第三版或（随你）更新的版本
# 我们希望发布的这款程序有用，但不保证，甚至不保证它有经济价值和适合特定用途。详情参见GNU通用公共许可协议
# 你理当已收到一份GNU通用公共许可协议的副本，如果没有，请查阅<http://www.gnu.org/licenses/>
# author：向昕哲

import draw_circle
import init_stars
import move_stars
import pygame
import text

# 初始化
pygame.init()
screen_width = 1280
screen_height = 720
screen_centrex = screen_width // 2 - 1
screen_centrey = screen_height // 2 - 1
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("模拟太阳系")
pause_button = pygame.image.load("../images/pause.jpg")
pause = False
time = 0

stars = init_stars.get_stars(screen)

clock = pygame.time.Clock()
running = True

#事件
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.MOUSEBUTTONDOWN == event.type and 0 <= event.pos[0] <= 85 and 60 <= event.pos[1] <= 145:
            if pause:
                pause = False
            else:
                pause = True

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (screen_centrex, screen_centrey), 30, 0)

    draw_circle.draw_circle(screen)

    # 暂停
    if not pause:
        move_stars.move_stars(stars, screen_centrex, screen_centrey)

        time += 1

        texts = text.get_texts(time)

    for i in (0, 1, 2, 3, 4, 5, 6, 7):
        stars[i].draw()

    # 在屏幕上打印
    screen.blit(pause_button, (0, 60))
    screen.blit(texts[0], texts[1])
    screen.blit(texts[2], (0, 33))
    screen.blit(texts[3], (0, 66))
    pygame.display.flip()
    clock.tick_busy_loop()

# 退出
pygame.quit()

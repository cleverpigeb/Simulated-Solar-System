#!python3
# -*- coding: UTF-8 -*-
# 版权所有 © 2019 向昕哲
# 本程序为自由软件，在自由软件联盟发布的GNU通用公共许可协议的约束下，你可以对其进行再发布及修改。协议版本为第三版或（随你）更新的版本
# 我们希望发布的这款程序有用，但不保证，甚至不保证它有经济价值和适合特定用途。详情参见GNU通用公共许可协议
# 你理当已收到一份GNU通用公共许可协议的副本，如果没有，请查阅<http://www.gnu.org/licenses/>
# author：向昕哲

import pygame

# 画轨道
def draw_circle(screen):
    pygame.draw.circle(screen, (255, 255, 0), (638, 358), 51, 1)
    pygame.draw.circle(screen, (255, 255, 0), (638, 358), 102, 1)
    pygame.draw.circle(screen, (255, 255, 0), (638, 358), 153, 1)
    pygame.draw.circle(screen, (255, 255, 0), (638, 358), 204, 1)
    pygame.draw.circle(screen, (255, 255, 0), (638, 358), 255, 1)
    pygame.draw.circle(screen, (255, 255, 0), (640, 358), 306, 1)
    pygame.draw.circle(screen, (255, 255, 0), (640, 358), 357, 1)
    pygame.draw.circle(screen, (255, 255, 0), (640, 358), 408, 1)

#!python3
# -*- coding: UTF-8 -*-
# 版权所有 © 2019 向昕哲
# 本程序为自由软件，在自由软件联盟发布的GNU通用公共许可协议的约束下，你可以对其进行再发布及修改。协议版本为第三版或（随你）更新的版本
# 我们希望发布的这款程序有用，但不保证，甚至不保证它有经济价值和适合特定用途。详情参见GNU通用公共许可协议
# 你理当已收到一份GNU通用公共许可协议的副本，如果没有，请查阅<http://www.gnu.org/licenses/>
# author：向昕哲

import numpy as np
import pygame

# 行星类
class Star(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, r, color, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2 * r, 2 * r))
        pygame.draw.circle(self.image, color, (r, r), r)
        self.image.set_colorkey((0,  0,  0))
        self.rect = self.image.get_rect()
        self.angle = 0
        self.screen = screen

    # 移动
    def move(self, x, y, radius, speed):
        self.speed = speed
        self.rect.centerx = x + radius * np.cos(np.radians(self.angle))
        self.rect.centery = y + radius * np.sin(np.radians(self.angle))
        self.angle = self.angle - self.speed

    # 在屏幕上打印
    def draw(self):
        self.screen.blit(self.image, self.rect)

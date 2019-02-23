#!python3
# -*- coding: UTF-8 -*-
# 版权所有 © 2019 向昕哲
# 本程序为自由软件，在自由软件联盟发布的GNU通用公共许可协议的约束下，你可以对其进行再发布及修改。协议版本为第三版或（随你）更新的版本
# 我们希望发布的这款程序有用，但不保证，甚至不保证它有经济价值和适合特定用途。详情参见GNU通用公共许可协议
# 你理当已收到一份GNU通用公共许可协议的副本，如果没有，请查阅<http://www.gnu.org/licenses/>
# author：向昕哲

import pygame

# 获取左上角的文字
def get_texts(time):
    font1_text = pygame.font.Font("../fonts/songti.ttf", 20)
    font1_render = font1_text.render("虚拟天数：" + str(int(time / 360 * 365.2422 + 0.5)), True, (255, 255, 255))
    font1_rect = font1_render.get_rect()

    font2_text = pygame.font.Font("../fonts/songti.ttf", 20)
    font2_render = font2_text.render("虚拟年数：" + str(round(time / 360, 2)), True, (255, 255, 255))

    font3_text = pygame.font.Font("../fonts/songti.ttf", 20)
    font3_render = font3_text.render("运行毫秒数：" + str(pygame.time.get_ticks()), True, (255, 255, 255))

    return (font1_render, font1_rect, font2_render, font3_render)

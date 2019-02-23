#!python3
# -*- coding: UTF-8 -*-
# 版权所有 © 2019 向昕哲
# 本程序为自由软件，在自由软件联盟发布的GNU通用公共许可协议的约束下，你可以对其进行再发布及修改。协议版本为第三版或（随你）更新的版本
# 我们希望发布的这款程序有用，但不保证，甚至不保证它有经济价值和适合特定用途。详情参见GNU通用公共许可协议
# 你理当已收到一份GNU通用公共许可协议的副本，如果没有，请查阅<http://www.gnu.org/licenses/>
# author：向昕哲

import star

# 初始化这些行星
def get_stars(screen):
    mercury = star.Star(15, (85, 0, 170), screen)
    venus = star.Star(15, (170, 43, 43), screen)
    earth = star.Star(15, (0, 0, 255), screen)
    mars = star.Star(15, (223, 0, 32), screen)
    jupiter = star.Star(15, (249, 236, 228), screen)
    saturn = star.Star(15, (237, 189, 101), screen)
    uranus = star.Star(15, (87, 250, 255), screen)
    neptune = star.Star(15, (143, 188, 143), screen)
    return (mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)

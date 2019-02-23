#!python3
# -*- coding: UTF-8 -*-
# 版权所有 © 2019 向昕哲
# 本程序为自由软件，在自由软件联盟发布的GNU通用公共许可协议的约束下，你可以对其进行再发布及修改。协议版本为第三版或（随你）更新的版本
# 我们希望发布的这款程序有用，但不保证，甚至不保证它有经济价值和适合特定用途。详情参见GNU通用公共许可协议
# 你理当已收到一份GNU通用公共许可协议的副本，如果没有，请查阅<http://www.gnu.org/licenses/>
# author：向昕哲

# 设置行星的移动
def move_stars(stars, screen_centrex, screen_centrey):
    stars[0].move(screen_centrex, screen_centrey, 51, 4.16)
    stars[1].move(screen_centrex, screen_centrey, 102, 1.63)
    stars[2].move(screen_centrex, screen_centrey, 153, 1)
    stars[3].move(screen_centrex, screen_centrey, 204, 0.53)
    stars[4].move(screen_centrex, screen_centrey, 255, 0.084)
    stars[5].move(screen_centrex, screen_centrey, 306, 0.034)
    stars[6].move(screen_centrex, screen_centrey, 357, 0.012)
    stars[7].move(screen_centrex, screen_centrey, 408, 0.0061)

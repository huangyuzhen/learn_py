#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PIL import Image

maze = Image.open("24/maze.png")
directions = [(0,1), (0,-1), (1,0), (-1,0)]
white = (255, 255, 255, 255)
w, h = maze.size

next_map = {}

entrance = (w - 2, 0)
exit = (1, h - 1)
queue = [exit]

while queue:
    pos = queue.pop(0)

    if pos == entrance:
        break
    for d in directions:
        tmp = (pos[0] + d[0], pos[1] + d[1])
        if not tmp in next_map and 0 <= tmp[0] < w and 0 <= tmp[1] < h and maze.getpixel(tmp) != white:
            next_map[tmp] = pos
            queue.append(tmp)


path = []
while pos != exit:
    # 最短路径上的点
    pixel = maze.getpixel(pos)
    # print(pos, pixel)
    path.append(pixel[0])
    pos = next_map[pos]

# skipping the 0s
# print(path[0::2])
with open('result.out','wb') as f:
    f.write(bytes(path[1::2]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： LiuYuZhao
# datetime： 2022/1/14 23:33

import pygame
import time
import sys


def draw_window(maze, block_size, block_list, treasure, route, best_route):
    window = pygame.display.set_mode((len(maze[0]) * block_size, len(maze) * block_size))
    pygame.display.set_caption("DFSRobot")

    i = 0
    j = 0
    search_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill((255, 255, 255))
        robot_color = (187, 255, 255)

        draw_blocks(window, block_list, block_size)
        draw_treasure(window, treasure, block_size)

        if not search_over:
            time.sleep(0.2)
            loc = route[i]
            i += 1
        if search_over:
            if j < len(best_route):
                time.sleep(0.05)
                loc = best_route[j]
                j += 1
        pygame.draw.rect(
            window, robot_color, (loc[1] * block_size, loc[0] * block_size, block_size - 8, block_size - 8), 0)

        if len(route) - 1 == i and search_over == False:
            print("机器人第{}次找到宝藏！".format(i + 1))
            search_over = True
        pygame.display.update()
        time.sleep(0.01)


def draw_blocks(window, block_lists, block_size):
    block_color = (255, 222, 173)
    for i in range(len(block_lists)):
        x, y = block_lists[i]
        position = (y * block_size, x * block_size, block_size - 5, block_size - 5)
        pygame.draw.rect(window, block_color, position, 0)


def draw_treasure(window, treasure, block_size):
    treasure_color = (255, 62, 150)
    position = (treasure[1] * block_size, treasure[0] * block_size, block_size - 5, block_size - 5)
    pygame.draw.rect(window, treasure_color, position, 0)

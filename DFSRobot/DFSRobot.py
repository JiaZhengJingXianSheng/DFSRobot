#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： LiuYuZhao
# datetime： 2022/1/14 23:50
from DFS import DFS_Route
from Draw import draw_window
from Maze import Maze

if __name__ == '__main__':
    maze = Maze()
    best_route, route = DFS_Route(maze.maze, maze.get_start(), maze.get_treasure())

    draw_window(maze.maze, 50, maze.set_blocks(),  maze.get_treasure(),route,best_route)

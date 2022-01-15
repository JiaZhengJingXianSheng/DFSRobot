#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： LiuYuZhao
# datetime： 2022/1/14 23:30


#   maze is 2-dim list
#   start is start location --> (i,j)
#   treasure is end location --> (i,j)
#   return is a route list

def DFS_Route(maze, start, treasure):
    max_row = len(maze) - 1
    max_col = len(maze[0]) - 1

    # maze[treasure[0]][treasure[1]] = 0
    lists = [start]
    route = []
    while lists:
        now = lists[-1]
        if now == treasure:
            route.append(lists[-1])

            break

        row, col = now
        maze[row][col] = 4

        route.append(lists[-1])


        if row != 0 and (maze[row - 1][col] == 0 or maze[row - 1][col] == 3):
            # up
            lists.append((row - 1, col))
            continue

        elif row != max_row and (maze[row + 1][col] == 0 or maze[row + 1][col] == 3):
            # down
            lists.append((row + 1, col))
            continue

        elif col != 0 and (maze[row][col - 1] == 0 or maze[row][col - 1] == 3):
            # left
            lists.append((row, col - 1))
            continue
        elif col != max_col and (maze[row][col + 1] == 0 or maze[row][col + 1] == 3):
            # right
            lists.append((row, col + 1))
            continue
        else:
            lists.pop()

    return lists, route

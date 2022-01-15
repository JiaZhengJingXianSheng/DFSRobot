# @Author: LiuYuZhao
# @Date: 2022-01-13

class Maze:
    def __init__(self):
        # self.maze = [
        #     [3, 2, 2, 2, 2, 2, 2, 2, 1],
        #     [0, 0, 2, 2, 2, 2, 2, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 2],
        #     [2, 2, 0, 0, 2, 0, 0, 2, 2],
        #     [2, 2, 2, 0, 2, 0, 2, 2, 2]]
        self.maze = [
            [2, 0, 0, 0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 0, 0, 1, 2],
            [2, 0, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
            [2, 0, 2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2, 0, 2],
            [2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 2],
            [2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2],
            [2, 2, 0, 0, 0, 2, 0, 0, 2, 0, 2, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2],
            [3, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2]
        ]

    def get_rows(self):
        return len(self.maze)

    def get_cols(self):
        return len(self.maze[0])

    # get start local
    # this function can be simplify
    def get_start(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 1:
                    return (i, j)

    # get treasure location
    def get_treasure(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 3:
                    return (i, j)

    # get blocks local list
    def set_blocks(self):
        self.block_lists = []
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 2:
                    self.block_lists.append((i, j))
        return self.block_lists

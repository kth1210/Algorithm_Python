import sys
from collections import deque

def calculate_minimum_move(maze):
    maze_row = len(maze)
    maze_col = len(maze[0])
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    queue = deque()
    queue.append((0, 0))

    while queue:
        current_row, current_col = queue.popleft()
        current_value = maze[current_row][current_col]

        for idx in range(4):
            next_row = current_row + dr[idx]
            next_col = current_col + dc[idx]
            
            if next_row >= 0 and next_row < maze_row and next_col >= 0 and next_col < maze_col:
                next_value = maze[next_row][next_col]

                if current_value + 1 < next_value or next_value == 1:
                    queue.append((next_row, next_col))
                    maze[next_row][next_col] = current_value + 1

    return maze[-1][-1]


def solution():
    N, M = map(int, sys.stdin.readline().split())
    maze = []

    for _ in range(N):
        input_maze = list(map(int, sys.stdin.readline().rstrip()))
        maze.append(input_maze)

    minimum_move = calculate_minimum_move(maze)
    print(minimum_move)

solution()
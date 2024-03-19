import sys
from collections import deque
from itertools import combinations

def BFS(boards, start_row, start_col):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    queue = deque()
    queue.append((0, 0, start_row, start_col, 1, boards[start_row][start_col]))
    max_value = 0

    while queue:
        pre_row, pre_col, cur_row, cur_col, cur_size, cur_value = queue.popleft()

        if cur_size == 4:
            max_value = max(max_value, cur_value)
            continue

        if cur_size == 2:
            cases = []
            for i in range(4):
                next_row = cur_row + dr[i]
                next_col = cur_col + dc[i]
                if 0 <= next_row < len(boards) and 0 <= next_col < len(boards[0]):
                    if next_row != pre_row or next_col != pre_col:
                        cases.append((next_row, next_col))

            for case in combinations(cases, 2):
                value = cur_value + boards[case[0][0]][case[0][1]] + boards[case[1][0]][case[1][1]]
                max_value = max(max_value, value)

        for idx in range(4):
            next_row = cur_row + dr[idx]
            next_col = cur_col + dc[idx]

            if 0 <= next_row < len(boards) and 0 <= next_col < len(boards[0]):
                if pre_row != next_row or pre_col != next_col:
                    next_value = cur_value + boards[next_row][next_col]
                    queue.append((cur_row, cur_col, next_row, next_col, cur_size + 1, next_value))
    
    return max_value

def solution():
    N, M = map(int, sys.stdin.readline().split())
    boards = []
    max_value = 0

    for _ in range(N):
        boards.append(list(map(int, sys.stdin.readline().split())))
    
    for row in range(N):
        for col in range(M):
            current_value = BFS(boards, row, col)
            max_value = max(max_value, current_value)
    
    print(max_value)

solution()

import sys
from collections import deque

def move_earth_worm(start_row, start_col, field):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    field_row = len(field)
    field_col = len(field[0])

    queue = deque()
    queue.append((start_row, start_col))
    field[start_row][start_col] = 0

    while queue:
        now_row, now_col = queue.popleft()

        for idx in range(4):
            next_row = now_row + dr[idx]
            next_col = now_col + dc[idx]

            if next_row < 0 or next_row >= field_row or next_col < 0 or next_col >= field_col:
                continue

            if field[next_row][next_col] == 1:
                queue.append((next_row, next_col))
                field[next_row][next_col] = 0

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        field_col, field_row, location_count = map(int, sys.stdin.readline().split())
        field = [[0 for _ in range(field_col)] for _ in range(field_row)]

        for _ in range(location_count):
            cabbage_col, cabbage_row = map(int, sys.stdin.readline().split())

            field[cabbage_row][cabbage_col] = 1
        
        earth_worm_count = 0
        for row_idx in range(field_row):
            for col_idx in range(field_col):
                if field[row_idx][col_idx] == 1:
                    earth_worm_count += 1
                    move_earth_worm(row_idx, col_idx, field)
        
        print(earth_worm_count)

solution()
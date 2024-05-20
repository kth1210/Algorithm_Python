import sys
from collections import deque
FILL = -1
EMPTY = 0

def calc_area(board, start_row, start_col):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    queue = deque()
    queue.append((start_row, start_col))
    area = 1
    board[start_row][start_col] = area

    while queue:
        cur_row, cur_col = queue.popleft()

        for idx in range(4):
            next_row = cur_row + dr[idx]
            next_col = cur_col + dc[idx]

            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                if board[next_row][next_col] == EMPTY:
                    area += 1
                    board[next_row][next_col] = area
                    queue.append((next_row, next_col))

    return area
                    

def solution():
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0 for _ in range(N)]for _ in range(M)]

    for _ in range(K):
        start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                board[y][x] = FILL
    
    areas = []
    for row in range(M):
        for col in range(N):
            if board[row][col] == EMPTY:
                area = calc_area(board, row, col)
                areas.append(area)
    
    print(len(areas))
    print(*sorted(areas))


solution()
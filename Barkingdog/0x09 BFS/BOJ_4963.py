import sys
from collections import deque
LAND = 1
SEA = 0

def land_to_sea(board, start_row, start_col):
    dr = [0, 0, 1, -1, 1, 1, -1, -1]
    dc = [-1, 1, 0, 0, 1, -1, 1, -1]
    queue = deque()
    queue.append((start_row, start_col))
    board[start_row][start_col] = SEA

    while queue:
        cur_row, cur_col = queue.popleft()

        for idx in range(8):
            next_row = cur_row + dr[idx]
            next_col = cur_col + dc[idx]

            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                if board[next_row][next_col] == LAND:
                    queue.append((next_row, next_col))
                    board[next_row][next_col] = SEA

def solution():
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w == h == 0:
            break

        board = []
        for _ in range(h):
            board.append(list(map(int, sys.stdin.readline().split())))
        
        count = 0
        for row in range(h):
            for col in range(w):
                if board[row][col] == LAND:
                    land_to_sea(board, row, col)
                    count += 1
        
        print(count)

solution()
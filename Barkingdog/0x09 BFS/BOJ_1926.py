import sys
from collections import deque

def calc_size(board, row, col):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    queue = deque()
    queue.append((row, col))
    board[row][col] = 0
    size = 1

    while queue:
        cur_row, cur_col = queue.popleft()

        for idx in range(4):
            next_row = cur_row + dr[idx]
            next_col = cur_col + dc[idx]

            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                if board[next_row][next_col] == 1:
                    board[next_row][next_col] = 0
                    size += 1
                    queue.append((next_row, next_col))
    
    return size

def solution():
    n, m = map(int, sys.stdin.readline().split())
    board = []

    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))
    
    painting_count = 0
    largest_size = 0
    
    for row in range(n):
        for col in range(m):
            if board[row][col] == 1:
                cur_size = calc_size(board, row, col)
                largest_size = max(largest_size, cur_size)
                painting_count += 1

    print(painting_count)
    print(largest_size)


solution()
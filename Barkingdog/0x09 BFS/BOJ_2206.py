import sys
from collections import deque
WALL = -1
NOT_VISITED = -1

def calc_distance(board, start_row, start_col, end_row, end_col):
    distances = [[NOT_VISITED for _ in range(len(board[0]))] for _ in range(len(board))]
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    queue = deque() # (행, 열, 벽 부쉈는지)
    queue.append((start_row, start_col, False))
    distances[start_row][start_col] = 1

    while queue:
        cur_row, cur_col, is_break = queue.popleft()
        cur_distance = distances[cur_row][cur_col]

        for idx in range(4):
            next_row = cur_row + dr[idx]
            next_col = cur_col + dc[idx]

            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                if board[next_row][next_col] != WALL:   # 다음이 벽이 아닐 때
                    if distances[next_row][next_col] == NOT_VISITED or cur_distance + 1 < distances[next_row][next_col]:
                        distances[next_row][next_col] = cur_distance + 1
                        queue.append((next_row, next_col, is_break))
                elif not is_break:  # 다음이 벽이지만 부술 수 있을 때
                    if distances[next_row][next_col] == NOT_VISITED or cur_distance + 1 < distances[next_row][next_col]:
                        distances[next_row][next_col] = cur_distance + 1
                        queue.append((next_row, next_col, True)) 
    
    return distances[end_row][end_col]

def solution():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    
    for _ in range(N):
        input_row = list(map(int, sys.stdin.readline().rstrip()))
        board.append([WALL if x == 1 else x for x in input_row])
    
    start_end_distance = calc_distance(board, 0, 0, N-1, M-1)
    end_start_distance = calc_distance(board, N-1, M-1, 0, 0)
    
    if start_end_distance == -1:
        print(end_start_distance)
    elif end_start_distance == -1:
        print(start_end_distance)
    else:
        print(min(start_end_distance, end_start_distance))

solution()
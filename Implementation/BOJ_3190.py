import sys
from collections import deque

def solution():
    N = int(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline().rstrip())
    board = [[False for _ in range(N)] for _ in range(N)]

    for _ in range(K):
        apple_row, apple_col = map(int, sys.stdin.readline().split())
        board[apple_row - 1][apple_col - 1] = True
    
    L = int(sys.stdin.readline().rstrip())
    moves = []
    
    for _ in range(L):
        input_move = sys.stdin.readline().split()
        moves.append([int(input_move[0]), input_move[1]])
    
    # 방향 전환이 끝나면 최대 N초 안에 끝남
    moves.append([moves[-1][0] + N, 'D'])

    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direction = 0
    snake = deque()
    time = 0
    cur_location = [0, 0]

    for move in moves:
        while time < move[0]:
            time += 1
            next_row = cur_location[0] + dr[direction]
            next_col = cur_location[1] + dc[direction]

            # 벽
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                print(time)
                return
            
            # 자기 자신
            if [next_row, next_col] in snake:
                print(time)
                return

            # 사과
            if board[next_row][next_col]:
                snake.append(cur_location)
                board[next_row][next_col] = False
            else:
                snake.append(cur_location)
                snake.popleft()
            
            cur_location = [next_row, next_col]
        
        if move[1] == 'D':
            direction = (direction + 1) % len(dr)
        elif move[1] == 'L':
            direction = direction - 1 if direction > 0 else len(dr) - 1

solution()
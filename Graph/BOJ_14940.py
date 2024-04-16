import sys
from collections import deque

def BFS(board, visited, start_location):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    queue = deque()
    queue.append(start_location)
    visited[start_location[0]][start_location[1]] = True

    while queue:
        current_location = queue.popleft()
        current_value = board[current_location[0]][current_location[1]]

        for idx in range(4):
            next_row = current_location[0] + dr[idx]
            next_col = current_location[1] + dc[idx]

            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                if not visited[next_row][next_col] and board[next_row][next_col] == 1:
                    board[next_row][next_col] = current_value + 1
                    queue.append([next_row, next_col])
                    visited[next_row][next_col] = True
    

def solution():
    n, m = map(int, sys.stdin.readline().split())
    board = []
    start_location = [0, 0]

    for row in range(n):
        input_row = list(map(int, sys.stdin.readline().split()))
        if 2 in input_row:
            start_location = [row, input_row.index(2)]
            input_row[input_row.index(2)] = 0
        board.append(input_row)

    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    BFS(board, visited, start_location)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1 and not visited[i][j]:
                board[i][j] = -1

    for row in board:        
        print(*row)

solution()

# 문제 정리
'''
각 지점에서 목표지점(2)까지의 거리
입력 받으면서 2를 찾고, 위치 저장함
    2는 0으로 변경함

2에서 시작이라고 생각하고, 저장한 위치에서 다음 위치로 BFS 사용 (1일 경우 이동)
    이동하는동안 이전 값 + 1 저장함
방문 여부를 저장하고, 원래 갈 수 있는 땅인데 도달할 수 없는 경우 -1로 변경
'''
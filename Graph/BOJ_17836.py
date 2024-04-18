import sys
from collections import deque

def solution():
    N, M, T = map(int, sys.stdin.readline().split())
    board = []
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    SWORD = -2
    WALL = -1
    PRINCESS_ROW = N - 1
    PRINCESS_COL = M - 1
    EMPTY = 0

    for _ in range(N):
        input_row = list(map(int, sys.stdin.readline().split()))
        input_row = [WALL if y == 1 else y for y in input_row]
        input_row = [SWORD if y == 2 else y for y in input_row]
        board.append(input_row)

    queue = deque()
    queue.append((0, 0))
    board[0][0] = 1

    while queue:
        cur_row, cur_col = queue.popleft()
        cur_time = board[cur_row][cur_col]
        
        for idx in range(4):
            next_row = cur_row + dr[idx]
            next_col = cur_col + dc[idx]

            if 0 <= next_row < N and 0 <= next_col < M:
                next_value = board[next_row][next_col]

                # 다음 위치가 검인 경우 최단 거리만 계산
                if next_value == SWORD:
                    distance = cur_time + 1 + abs(next_row - PRINCESS_ROW) + abs(next_col - PRINCESS_COL)
                    princess_time = board[PRINCESS_ROW][PRINCESS_COL]
                    if princess_time == EMPTY or princess_time > distance:
                        board[PRINCESS_ROW][PRINCESS_COL] = distance
                elif next_value == EMPTY or next_value > cur_time + 1:
                    board[next_row][next_col] = cur_time + 1
                    queue.append((next_row, next_col))
    
    # 시작 시간이 1이었던 것에 대한 보상
    # 도달하지 못하는 경우, 시간 초과된 경우 처리
    if board[PRINCESS_ROW][PRINCESS_COL] - 1 > T or board[PRINCESS_ROW][PRINCESS_COL] == EMPTY:
        print("Fail")
    else:
        print(board[PRINCESS_ROW][PRINCESS_COL] - 1)

    
solution()


'''
T시간 이내로 만나지 못하면 안됨
만약에 검을 구하면 벽 무시하고 이동할 수 있음
    그 말은 검을 구하면 그 위치에서 공주한테 최단거리로 이동할 수 있다는 뜻

BFS로 처음부터 탐색
    꺼낸 칸이 검이라면?
        여기서부터 공주 위치까지 최단 거리 구해서 공주 위치에 넣음 (더 작으면)
    다음 칸이 벽이 아니라면 이동하면서 시간 저장
'''
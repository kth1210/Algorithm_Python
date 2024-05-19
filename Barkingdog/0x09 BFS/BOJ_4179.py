import sys
from collections import deque

def solution():
    R, C = map(int, sys.stdin.readline().split())
    board = []
    fire_queue = deque()    # (시간, 행, 열)
    jihun_queue = deque()   # (시간, 행, 열)
    JIHUN = "J"
    FIRE = "F"
    WALL = "#"
    MOVABLE = "."
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    for row in range(R):
        input_row = list(sys.stdin.readline().rstrip())
        for col in range(C):
            if input_row[col] == JIHUN:
                jihun_queue.append((0, row, col))
            elif input_row[col] == FIRE:
                fire_queue.append((0, row, col))
        board.append(input_row)
    
    time = 0
    jihun_count = len(jihun_queue)
    while True:        
        # 지훈 이동
        while jihun_queue and jihun_queue[0][0] == time:
            cur_time, cur_row, cur_col = jihun_queue.popleft()
            jihun_count -= 1

            # 이미 불 탄 경우
            if board[cur_row][cur_col] == FIRE:
                continue

            for idx in range(4):
                next_row = cur_row + dr[idx]
                next_col = cur_col + dc[idx]

                if 0 <= next_row < R and 0 <= next_col < C:
                    if board[next_row][next_col] == MOVABLE:
                        board[next_row][next_col] = JIHUN
                        jihun_queue.append((cur_time + 1, next_row, next_col))
                        jihun_count += 1
                else:
                    print(cur_time + 1)
                    return

        # 불 번지기
        while fire_queue and fire_queue[0][0] == time:
            cur_time, cur_row, cur_col = fire_queue.popleft()

            for idx in range(4):
                next_row = cur_row + dr[idx]
                next_col = cur_col + dc[idx]

                if 0 <= next_row < R and 0 <= next_col < C:
                    if board[next_row][next_col] == MOVABLE or board[next_row][next_col] == JIHUN:
                        board[next_row][next_col] = FIRE
                        fire_queue.append((cur_time + 1, next_row, next_col))

                        if board[next_row][next_col] == JIHUN:
                            jihun_count -= 1

        # 이동할 수 있는 지훈이가 없다면 불가
        if jihun_count == 0:
            print("IMPOSSIBLE")
            return
        
        time += 1


solution()

'''
미로
지훈, 불 위치
지훈이가 불에 타기 전에 탈출할 수 있나?
탈출하는데 얼마나 걸리나?
미로의 가장자리에서 탈출 가능
    queue에서 뽑았을 때 다음 위치가 범위 밖이라면 탈출 (시간 + 1)

1분마다 지훈, 불 이동
불은 있는데 지훈이는 없으면 IMPOSSIBLE
불 번지게 한 다음
지훈이 모든 위치에 대해서 이동
    다음 위치가 탈출 가능하면 탈출하고 끝
'''
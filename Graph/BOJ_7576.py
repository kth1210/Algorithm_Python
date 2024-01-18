import sys
from collections import deque

def BFS(ripen_tomatoes, box):
    box_row = len(box)
    box_col = len(box[0])
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    queue = deque(ripen_tomatoes)

    while queue:
        now_row, now_col = queue.popleft()

        for idx in range(4):
            next_row = now_row + dr[idx]
            next_col = now_col + dc[idx]

            if next_row < 0 or next_row >= box_row or next_col < 0 or next_col >= box_col:
                continue
        
            if box[next_row][next_col] == 0:
                box[next_row][next_col] = box[now_row][now_col] + 1
                queue.append((next_row, next_col))


def solution():
    box_col, box_row = map(int, sys.stdin.readline().split())
    box = []

    for _ in range(box_row):
        box.append(list(map(int, sys.stdin.readline().split())))
    
    ripen_tomatoes = []
    for row in range(box_row):
        for col in range(box_col):
            if box[row][col] == 1:
                ripen_tomatoes.append((row, col))
    
    BFS(ripen_tomatoes, box)

    day = 0
    for row in box:
        if 0 in row:
            print(-1)
            return
        else:
            day = max(max(row), day)
    
    if day == 1:
        print(0)
    else:
        # 익은 토마토의 시작이 1인 것에 대한 보상
        print(day - 1)

solution()
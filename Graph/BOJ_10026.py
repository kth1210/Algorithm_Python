import sys
from collections import deque

def BFS(picture, start_row, start_col):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    picture_row = len(picture)
    picture_col = len(picture[0])
    start_color = picture[start_row][start_col]
    queue = deque()
    queue.append((start_row, start_col))
    picture[start_row][start_col] = 'X'

    while queue:
        current_row, current_col = queue.popleft()

        for idx in range(4):
            next_row = current_row + dr[idx]
            next_col = current_col + dc[idx]

            if next_row < 0 or next_row >= picture_row or next_col < 0 or next_col >= picture_col:
                continue
                
            if picture[next_row][next_col] == start_color:
                queue.append((next_row, next_col))
                picture[next_row][next_col] = 'X'

def solution():
    N = int(sys.stdin.readline().rstrip())
    picture = []
    weakness_picture = []

    for _ in range(N):
        input_picture = sys.stdin.readline().rstrip()
        picture.append(list(input_picture))
        weakness_picture.append(list(input_picture.replace("G", "R")))

    picture_area_count = 0
    weakness_picture_area_count = 0
    for row in range(N):
        for col in range(N):
            if picture[row][col] != 'X':
                BFS(picture, row, col)
                picture_area_count += 1
            
            if weakness_picture[row][col] != 'X':
                BFS(weakness_picture, row, col)
                weakness_picture_area_count += 1

    print(picture_area_count, end = ' ')
    print(weakness_picture_area_count)

solution()
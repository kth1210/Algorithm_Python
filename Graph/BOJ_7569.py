import sys
from collections import deque

def find_minimum_day(box):
    minimum_day = -1
    
    for floor in box:
        for row in floor:
            minimum_day = max(minimum_day, max(row))

            # 모두 익지 못하는 상황이면 -1 반환
            if 0 in row:
                return -1
    
    # 저장될 때부터 모든 토마토가 익어있는 상태면 0 반환
    if minimum_day == 1:
        return 0
    else:
        # 첫날 익은 토마토의 시작이 1인 것에 대한 보상
        return minimum_day - 1

def calculate_minimum_day_for_ripen(box, ripen_tomatoes):
    moves = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1)
    ]
    box_height = len(box)
    box_row = len(box[0])
    box_col = len(box[0][0])

    queue = deque(ripen_tomatoes)

    while queue:
        current_height, current_row, current_col = queue.popleft()
        current_tomato_value = box[current_height][current_row][current_col]

        for move in moves:
            next_height = current_height + move[0]
            next_row = current_row + move[1]
            next_col = current_col + move[2]

            if next_height < 0 or next_height >= box_height or next_row < 0 or next_row >= box_row or next_col < 0 or next_col >= box_col:
                continue

            if box[next_height][next_row][next_col] == 0:
                box[next_height][next_row][next_col] = current_tomato_value + 1
                queue.append((next_height, next_row, next_col))

    minimum_day = find_minimum_day(box)

    return minimum_day

def solution():
    box_col, box_row, box_height = map(int, sys.stdin.readline().split())
    box = [[] for _ in range(box_height)]

    for height in range(box_height):
        for _ in range(box_row):
            input_row = list(map(int, sys.stdin.readline().split()))
            box[height].append(input_row)

    ripen_tomatoes = []
    for height in range(box_height):
        for row in range(box_row):
            for col in range(box_col):
                if box[height][row][col] == 1:
                    ripen_tomatoes.append((height, row, col))

    minimum_day = calculate_minimum_day_for_ripen(box, ripen_tomatoes)

    print(minimum_day)

solution()
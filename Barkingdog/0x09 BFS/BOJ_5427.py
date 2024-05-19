import sys
from collections import deque

def calc_count_for_escape(building, start_row, start_col, fire_locations):
    PERSON = "@"
    FIRE = "*"
    EMPTY = "."
    WALL = "#"
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    person_queue = deque([(start_row, start_col)])
    fire_queue = deque(fire_locations)
    time = 0
    
    while True:
        time += 1
        person_count = len(person_queue)
        next_person_queue = deque()
        next_fire_queue = deque()

        while person_queue:
            cur_row, cur_col = person_queue.popleft()
            person_count -= 1

            if building[cur_row][cur_col] == FIRE:
                continue

            for idx in range(4):
                next_row = cur_row + dr[idx]
                next_col = cur_col + dc[idx]

                if 0 <= next_row < len(building) and 0 <= next_col < len(building[0]):
                    if building[next_row][next_col] == EMPTY:
                        building[next_row][next_col] = PERSON
                        next_person_queue.append((next_row, next_col))
                        person_count += 1
                else:
                    return time
        
        while fire_queue:
            cur_row, cur_col = fire_queue.popleft()

            for idx in range(4):
                next_row = cur_row + dr[idx]
                next_col = cur_col + dc[idx]

                if 0 <= next_row < len(building) and 0 <= next_col < len(building[0]):
                    if building[next_row][next_col] in (EMPTY, PERSON):
                        building[next_row][next_col] = FIRE
                        next_fire_queue.append((next_row, next_col))

                        if building[next_row][next_col] == PERSON:
                            person_count -= 1

        # 탈출할 수 없는 경우 -1 반환
        if person_count == 0:
            return -1

        person_queue = next_person_queue
        fire_queue = next_fire_queue


def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        w, h = map(int, sys.stdin.readline().split())
        building = []
        fire_locations = []
        start_row = 0
        start_col = 0

        for row in range(h):
            input_row = list(sys.stdin.readline().rstrip())

            for col in range(w):
                if input_row[col] == "@":
                    start_row = row
                    start_col = col
                elif input_row[col] == "*":
                    fire_locations.append((row, col))

            building.append(input_row)
        
        count = calc_count_for_escape(building, start_row, start_col, fire_locations)
        print(count if count != -1 else "IMPOSSIBLE")


solution()
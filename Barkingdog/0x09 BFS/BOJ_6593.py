import sys
from collections import deque
GOLD = "#"
EMPTY = "."
DESTINATION = "E"

def calc_escape_time(building, start_location):
    moves = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]   # 동, 서, 남, 북, 상, 하
    visited = [[[False for _ in range(len(building[0][0]))] for _ in range(len(building[0]))] for _ in range(len(building))]
    queue = deque()
    queue.append((0, start_location[0], start_location[1], start_location[2])) # 이동 횟수, 층, 행, 열
    visited[start_location[0]][start_location[1]][start_location[2]] = True

    while queue:
        cur_count, cur_floor, cur_row, cur_col = queue.popleft()

        for floor, row, col in moves:
            next_floor = cur_floor + floor
            next_row = cur_row + row
            next_col = cur_col + col

            if 0 <= next_floor < len(building) and 0 <= next_row < len(building[0]) and 0 <= next_col < len(building[0][0]):
                if building[next_floor][next_row][next_col] == DESTINATION:
                    return cur_count + 1
                
                if building[next_floor][next_row][next_col] == EMPTY and not visited[next_floor][next_row][next_col]:
                    visited[next_floor][next_row][next_col] = True
                    queue.append((cur_count + 1, next_floor, next_row, next_col))

    return -1


def solution():
    while True:
        L, R, C = map(int, sys.stdin.readline().split())
        if [L, R, C] == [0, 0, 0]:
            break
        
        building = []
        for floor in range(L):
            cur_floor = []
            for row in range(R):
                input_row = list(sys.stdin.readline().rstrip())
                for col in range(C):
                    if input_row[col] == "S":
                        start_location = (floor, row, col)
                cur_floor.append(input_row)
            building.append(cur_floor)
            _ = sys.stdin.readline()
        
        time = calc_escape_time(building, start_location)
        if time == -1:
            print("Trapped!")
        else:
            print(f"Escaped in {time} minute(s).")


solution()
import sys
from collections import deque
from itertools import combinations

# 안전 영역의 크기 계산
def calculate_safe_area(virus_map):
    count = 0
    for row in virus_map:
        count += row.count(0)
    return count

def spread_virus(virus_map):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    virus_map_row = len(virus_map)
    virus_map_col = len(virus_map[0])
    virus_location = []

    for row in range(virus_map_row):
        for col in range(virus_map_col):
            if virus_map[row][col] == 2:
                virus_location.append((row, col))
    
    queue = deque(virus_location)

    while queue:
        current_virus_row, current_virus_col = queue.popleft()

        for idx in range(4):
            next_virus_row = current_virus_row + dr[idx]
            next_virus_col = current_virus_col + dc[idx]

            if next_virus_row < 0 or next_virus_row >= virus_map_row or next_virus_col < 0 or next_virus_col >= virus_map_col:
                continue

            if virus_map[next_virus_row][next_virus_col] == 0:
                virus_map[next_virus_row][next_virus_col] = 2
                queue.append((next_virus_row, next_virus_col))    

def solution():
    map_row, map_col = map(int, sys.stdin.readline().split())
    virus_map = []
    safe_areas = []

    for _ in range(map_row):
        input_row = list(map(int, sys.stdin.readline().split()))
        virus_map.append(input_row)

    for row in range(map_row):
        for col in range(map_col):
            if virus_map[row][col] == 0:
                safe_areas.append((row, col))
    
    all_cases_of_wall = list(combinations(safe_areas, 3))
    
    max_safe_area_count = 0
    for case_of_wall in all_cases_of_wall:
        current_virus_map = [row[:] for row in virus_map]

        for (row, col) in case_of_wall:
            current_virus_map[row][col] = 1

        spread_virus(current_virus_map)
        current_safe_area_count = calculate_safe_area(current_virus_map)
        max_safe_area_count = max(max_safe_area_count, current_safe_area_count)

    print(max_safe_area_count)
    
solution()
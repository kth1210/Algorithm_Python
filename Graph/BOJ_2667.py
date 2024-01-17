import sys
from collections import deque

def calculate_complex_count(house_row, house_col, complex_graph):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]
    complex_row = len(complex_graph)
    complex_col = len(complex_graph[0])

    queue = deque()
    queue.append((house_row, house_col))
    complex_graph[house_row][house_col] = 0
    count = 1

    while queue:
        now_row, now_col = queue.popleft()

        for idx in range(4):
            next_row = now_row + dr[idx]
            next_col = now_col + dc[idx]

            if next_row < 0 or next_row >= complex_row or next_col < 0 or next_col >= complex_col:
                continue

            if complex_graph[next_row][next_col] == 1:
                count += 1
                queue.append((next_row, next_col))
                complex_graph[next_row][next_col] = 0

    return count

def solution():
    N = int(sys.stdin.readline().rstrip())
    complex_graph = []

    for _ in range(N):
        complex_graph.append(list(map(int, sys.stdin.readline().rstrip())))
    
    complex_count_list = []
    for row_idx in range(N):
        for col_idx in range(N):
            if complex_graph[row_idx][col_idx] == 1:
                complex_count = calculate_complex_count(row_idx, col_idx, complex_graph)
                complex_count_list.append(complex_count)

    print(len(complex_count_list))
    for count in sorted(complex_count_list):
        print(count)

solution()
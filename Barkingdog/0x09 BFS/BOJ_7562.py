import sys
from collections import deque

def BFS(l, start, destination):
    if start == destination:
        return 0
    
    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    visited = [[False for _ in range(l)] for _ in range(l)]
    queue = deque() # (이동 수, 행, 열)
    queue.append((0, start[0], start[1]))
    visited[start[0]][start[1]] = True

    while queue:
        cur_count, cur_row, cur_col = queue.popleft()

        for move_row, move_col in moves:
            next_row = cur_row + move_row
            next_col = cur_col + move_col

            if 0 <= next_row < l and 0 <= next_col < l:
                if [next_row, next_col] == destination:
                    return cur_count + 1
                
                if not visited[next_row][next_col]:
                    queue.append((cur_count + 1, next_row, next_col))
                    visited[next_row][next_col] = True

    return -1

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        l = int(sys.stdin.readline().rstrip())
        start = list(map(int, sys.stdin.readline().split()))
        destination = list(map(int, sys.stdin.readline().split()))
        
        count = BFS(l, start, destination)
        print(count)

solution()
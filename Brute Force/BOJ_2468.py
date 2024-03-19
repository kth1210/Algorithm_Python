import sys
sys.setrecursionlimit(10 ** 6)

def DFS(heights, visited, start_row, start_col, current_height):
    if start_row < 0 or start_row >= len(heights) or start_col < 0 or start_col >= len(heights):
        return
    
    if visited[start_row][start_col] or heights[start_row][start_col] <= current_height:
        return
    
    visited[start_row][start_col] = True
    
    DFS(heights, visited, start_row + 1, start_col, current_height)
    DFS(heights, visited, start_row, start_col + 1, current_height)
    DFS(heights, visited, start_row - 1, start_col, current_height)
    DFS(heights, visited, start_row, start_col - 1, current_height)


def solution():
    N = int(sys.stdin.readline().rstrip())
    heights = []
    max_height = 0
    max_section_count = 0

    for _ in range(N):
        input_row = list(map(int, sys.stdin.readline().split()))
        heights.append(input_row)
        max_height = max(max_height, max(input_row))
    
    for current_height in range(max_height):
        section_count = 0
        visited = [[False for _ in range(N)] for _ in range(N)]

        for row in range(N):
            for col in range(N):
                if not visited[row][col] and heights[row][col] > current_height:
                    section_count += 1
                    DFS(heights, visited, row, col, current_height)

        max_section_count = max(max_section_count, section_count)

    print(max_section_count)

solution()
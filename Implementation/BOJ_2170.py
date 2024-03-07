import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    coordinates = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        coordinates.append((x, y))
    
    coordinates.sort()

    start = 0
    end = 0
    total_length = 0
    for x, y in coordinates:
        if start <= x <= end:
            end = max(end, y)
        else:
            total_length += end - start
            start = x
            end = y
    
    total_length += end - start

    print(total_length)

solution()
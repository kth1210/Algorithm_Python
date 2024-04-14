import sys

def solution():
    N, K = map(int, sys.stdin.readline().split())
    heights = list(map(int, sys.stdin.readline().split()))
    gaps = []

    for idx in range(1, len(heights)):
        gaps.append(heights[idx] - heights[idx - 1])
    
    gaps.sort()

    answer = sum(gaps[:N - K])
    print(answer)

solution()
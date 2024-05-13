import sys
from collections import deque

def solution():
    N, K = map(int, sys.stdin.readline().split())
    queue = deque([number for number in range(1, N + 1)])
    answer = []

    while queue:
        queue.rotate(-K + 1)
        answer.append(queue.popleft())
    
    print(f"<{', '.join(map(str, answer))}>")

solution()
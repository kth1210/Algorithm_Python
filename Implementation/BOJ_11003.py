import sys
from collections import deque

def solution():
    N, L = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    
    # queue에는 (인덱스, 값)이 저장됨
    queue = deque()

    for idx, number in enumerate(numbers):
        while queue and queue[-1][1] > number:
            queue.pop()
        
        while queue and queue[0][0] < idx - L + 1:
            queue.popleft()

        queue.append((idx, number))

        print(queue[0][1], end = ' ')

solution()
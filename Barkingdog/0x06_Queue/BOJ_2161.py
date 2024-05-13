import sys
from collections import deque

def solution():
    N = int(sys.stdin.readline().rstrip())
    queue = deque([number for number in range(1, N + 1)])

    while len(queue) > 1:
        print(queue.popleft(), end = " ")
        queue.rotate(-1)
        
    print(queue[0])

solution()
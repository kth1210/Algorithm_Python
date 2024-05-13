import sys
from collections import deque

def solution():
    n, w, L = map(int, sys.stdin.readline().split())
    weights = list(map(int, sys.stdin.readline().split()))
    bridge = deque([0 for _ in range(w)])
    current_weight = 0
    time = 0

    for weight in weights:
        time += 1
        current_weight -= bridge.popleft()
        
        while current_weight + weight > L:
            time += 1
            current_weight -= bridge.popleft()
            bridge.append(0)

        bridge.append(weight)
        current_weight += weight
    
    while current_weight > 0:
        time += 1
        current_weight -= bridge.popleft()
    
    print(time)


solution()
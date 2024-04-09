import sys
from collections import deque

def solution():
    N, K = map(int, sys.stdin.readline().split())
    numbers = deque([number for number in range(1, N + 1)])
    answer = []

    while numbers:
        numbers.rotate(-K + 1)
        answer.append(numbers.popleft())

    print(f"<{', '.join(map(str, answer))}>")    
    
solution()
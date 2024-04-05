import sys

def solution():
    N, L = map(int, sys.stdin.readline().split())
    puddles = []

    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        puddles.append((start, end))
    
    puddles.sort()

    answer = 0
    right = 0
    for puddle in puddles:
        start = puddle[0]
        end = puddle[1]

        if right < start:
            right = start

        diff = end - right
        count = (diff + L - 1) // L
        answer += count
        right += count * L
    
    print(answer)


solution()
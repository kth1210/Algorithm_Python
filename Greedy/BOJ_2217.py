import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    ropes = []

    for _ in range(N):
        ropes.append(int(sys.stdin.readline().rstrip()))
    
    ropes.sort(reverse = True)
    result = 0
    for idx, rope in enumerate(ropes):
        result = max(result, rope * (idx + 1))

    print(result)
    
solution()
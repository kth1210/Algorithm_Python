import sys

def nCr(n, r):
    upper = 1
    for _ in range(r):
        upper *= n
        n -= 1
    
    lower = 1
    for _ in range(r):
        lower *= r
        r -= 1
    
    return upper // lower

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        print(nCr(M, N))

solution()
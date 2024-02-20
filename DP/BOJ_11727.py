import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    cache = [0] * n
    cache[0] = 1
    
    if n >= 2:
        cache[1] = 3
        for idx in range(2, n):
            cache[idx] = (cache[idx-2] * 2 + cache[idx-1]) % 10_007
    
    print(cache[n-1])

solution()
import sys

def solution():
    n, k = map(int, sys.stdin.readline().split())
    coins = []

    for _ in range(n):
        coins.append(int(sys.stdin.readline().rstrip()))
    
    cache = [0 for _ in range(k + 1)]
    for coin in coins:
        if coin <= len(cache):
            cache[coin] += 1
        for cost in range(coin + 1, k + 1):
            cache[cost] += cache[cost - coin]
    
    print(cache[k])

solution()

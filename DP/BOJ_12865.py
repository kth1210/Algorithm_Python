import sys

def solution():
    N, K = map(int, sys.stdin.readline().split())
    things = []
    for _ in range(N):
        things.append(list(map(int, sys.stdin.readline().split())))

    dp = [0 for _ in range(K + 1)]
    for idx in range(len(things)):
        weight, value = things[idx]

        for pointer in range(K, weight - 1, -1):
            dp[pointer] = max(dp[pointer], dp[pointer - weight] + value)
    
    print(max(dp))

solution()
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    sequence = list(map(int, sys.stdin.readline().split()))
    dp = [0] * n
    dp[0] = sequence[0]

    for idx in range(1, n):
        dp[idx] = max(sequence[idx], dp[idx-1] + sequence[idx])

    print(max(dp))

solution()
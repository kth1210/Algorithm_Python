import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    dp = [0 for _ in range(N + 1)]
    
    if N < 3:
        print(1)
    else:
        dp[1] = 1
        dp[2] = 1

        for idx in range(3, N + 1):
            dp[idx] = dp[idx - 1] + dp[idx - 2]
        
        print(dp[N])

solution()
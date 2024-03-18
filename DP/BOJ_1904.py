import sys

def solution(N):
    dp = [0 for _ in range(N + 1)]
    
    if N < 3:
        print(N)
    else:
        dp[1] = 1
        dp[2] = 2

        for idx in range(3, N + 1):
            dp[idx] = (dp[idx - 2] + dp[idx - 1]) % 15_746
        
        print(dp[N])

N = int(sys.stdin.readline().rstrip())
solution(N)
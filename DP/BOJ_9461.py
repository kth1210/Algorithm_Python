import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        dp = [0] * (N+1)
        if 1 <= N <= 3:
            print(1)
        elif 4 <= N <= 5:
            print(2)
        else:
            dp[0] = 1
            dp[1] = 1
            dp[2] = 1
            dp[3] = 2
            dp[4] = 2

            for idx in range(5, N+1):
                dp[idx] = dp[idx-5] + dp[idx-1]
            
            print(dp[N-1])
        
solution()
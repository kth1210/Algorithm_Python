import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    amounts = []
    dp = [0] * n

    for _ in range(n):
        amounts.append(int(sys.stdin.readline().rstrip()))

    dp[0] = amounts[0]
    if n > 1:
        dp[1] = amounts[0] + amounts[1]
    
    if n > 2:
        dp[2] = max(amounts[2] + amounts[1], amounts[2] + dp[0], dp[1])

        for idx in range(3, n):
            # 현재, 이전 와인을 마시는 경우 / 현재 와인만 마시는 경우 / 현재 와인 안마시는 경우
            dp[idx] = max(amounts[idx] + amounts[idx-1] + dp[idx-3], amounts[idx] + dp[idx-2], dp[idx-1])
    
    print(dp[n-1])

solution()
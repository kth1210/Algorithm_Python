import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    dp = [0] * n
    dp[0] = int(sys.stdin.readline().rstrip())

    for row in range(1, n):
        input_triangle = list(map(int, sys.stdin.readline().split()))
        temp = [0] * n

        for col in range(row):
            temp[col] = max(temp[col], input_triangle[col] + dp[col])
            temp[col+1] = dp[col] + input_triangle[col+1]
        
        dp = temp

    print(max(dp))

solution()
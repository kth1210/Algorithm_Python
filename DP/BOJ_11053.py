import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().split()))
    dp = [1] * N

    for current_idx in range(1, N):
        for compare_idx in range(current_idx):
            if A[current_idx] > A[compare_idx]:
                dp[current_idx] = max(dp[current_idx], dp[compare_idx] + 1)
    
    print(max(dp))

solution()
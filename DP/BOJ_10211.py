import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        numbers = list(map(int, sys.stdin.readline().split()))
        dp = [0] * N
        dp[0] = numbers[0]

        for idx in range(1, N):
            # 이전의 합을 가져가느냐 마느냐 (음수인 경우 처리)
            dp[idx] = max(numbers[idx], dp[idx-1] + numbers[idx])
        
        print(max(dp))

solution()
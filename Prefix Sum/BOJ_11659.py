import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    prefix_sum = [0] * (N+1)

    for idx in range(N):
        prefix_sum[idx+1] = numbers[idx] + prefix_sum[idx]
    
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        answer = prefix_sum[j] - prefix_sum[i-1]
        print(answer)

solution()
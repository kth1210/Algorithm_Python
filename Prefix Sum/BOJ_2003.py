import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    prefix_sum = [0] * (N+1)

    for idx in range(N):
        prefix_sum[idx+1] = numbers[idx] + prefix_sum[idx]
    
    count = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if prefix_sum[j] - prefix_sum[i] == M:
                count += 1
    
    print(count)

solution()
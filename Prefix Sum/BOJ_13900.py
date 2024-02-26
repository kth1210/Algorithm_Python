import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    prefix_sum = [0 for _ in range(N+1)]

    for idx in range(1, N+1):
        prefix_sum[idx] = numbers[idx-1] + prefix_sum[idx-1]
    
    answer = 0
    for idx in range(2, N+1):
        answer += numbers[idx-1] * prefix_sum[idx-1]
    
    print(answer)

solution()
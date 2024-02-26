import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))
    prefix_sum = [0 for _ in range(N+1)]

    for idx in range(1, N+1):
        prefix_sum[idx] = prefix_sum[idx-1] + numbers[idx-1]
    
    M = int(sys.stdin.readline().rstrip())
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        answer = prefix_sum[j] - prefix_sum[i-1]
        print(answer)
        
solution()
import sys

def solution():
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())
        numbers = list(map(int, sys.stdin.readline().split()))
        prefix_sum = [0 for _ in range(N+1)]

        for idx in range(1, N+1):
            prefix_sum[idx] = numbers[idx-1] + prefix_sum[idx-1]
        
        maximum = numbers[0]
        for i in range(N+1):
            for j in range(i+1, N+1):
                value = prefix_sum[j] - prefix_sum[i]
                maximum = max(value, maximum)
        
        print(maximum)

solution()  
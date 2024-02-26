import sys

def solution():
    N, X = map(int, sys.stdin.readline().split())
    visitors = list(map(int, sys.stdin.readline().split()))
    prefix_sum = [0 for _ in range(N+1)]

    for idx in range(1, N+1):
        prefix_sum[idx] = prefix_sum[idx-1] + visitors[idx-1]
    
    max_count = 0
    period_count = 0
    for idx in range(1, N+1-X+1):
        visitor_count = prefix_sum[idx+X-1] - prefix_sum[idx-1]
        if visitor_count > max_count:
            max_count = visitor_count
            period_count = 1
        elif visitor_count == max_count:
            period_count += 1

    if max_count == 0:
        print("SAD")
    else:
        print(max_count)
        print(period_count)

solution()
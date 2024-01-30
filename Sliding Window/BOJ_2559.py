import sys

def solution():
    N, K = map(int, sys.stdin.readline().split())
    temperatures = list(map(int, sys.stdin.readline().split()))

    current_sum = sum(temperatures[:K])
    results = [current_sum]

    for day in range(1, N-K+1):
        current_sum += temperatures[day+K-1] - temperatures[day-1]
        results.append(current_sum)
    
    print(max(results))
    
solution()
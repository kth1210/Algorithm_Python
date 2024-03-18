import sys

def solution(count, costs):
    cache = [0 for _ in range(count + 1)]

    for current_count in range(1, count + 1):
        for idx in range(1, current_count + 1):
            cache[current_count] = max(cache[current_count], cache[current_count - idx] + costs[idx - 1])

    print(cache[count])

'''
input, test case
'''
N = int(sys.stdin.readline().rstrip())
costs = list(map(int, sys.stdin.readline().split()))
solution(N, costs)
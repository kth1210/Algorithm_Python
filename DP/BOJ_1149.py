import sys

def solution():
    N = int(sys.stdin.readline().rstrip())
    color_costs = []

    for _ in range(N):
        input_color_costs = list(map(int, sys.stdin.readline().split()))
        color_costs.append(input_color_costs)
    
    for idx in range(1, N):
        previous_color_costs = color_costs[idx - 1]
        color_costs[idx][0] += min(previous_color_costs[1], previous_color_costs[2])
        color_costs[idx][1] += min(previous_color_costs[0], previous_color_costs[2])
        color_costs[idx][2] += min(previous_color_costs[0], previous_color_costs[1])
    
    print(min(color_costs[N - 1]))

solution()
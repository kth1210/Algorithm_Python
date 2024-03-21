import sys
from collections import deque
INF = sys.maxsize

def find_minimum_cost(graph, costs, start, end):
    queue = deque()
    queue.append((start, 0))
    costs[start] = 0

    while queue:
        cur_city, cur_cost = queue.popleft()

        if costs[cur_city] < cur_cost:
            continue

        for next_city, next_cost in graph[cur_city]:
            cost = cur_cost + next_cost
            if cost < costs[next_city]:
                costs[next_city] = cost
                queue.append((next_city, cost))
    
    return costs[end]

def solution():
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    graph = {node:[] for node in range(N + 1)}
    costs = [INF for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append((end, cost))
    
    start_city, end_city = map(int, sys.stdin.readline().split())

    minimum_cost = find_minimum_cost(graph, costs, start_city, end_city)
    print(minimum_cost)

solution()
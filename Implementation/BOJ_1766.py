import sys
import heapq

'''
위상 정렬 + 우선순위 큐
'''
def solution():
    N, M = map(int, sys.stdin.readline().split())
    graph = {num:[] for num in range(1, N + 1)}
    in_degree = [0 for _ in range(N + 1)]
    heap = []
    sequence = []

    for _ in range(M):
        first, second = map(int, sys.stdin.readline().split())
        in_degree[second] += 1
        graph[first].append(second)

    for idx in range(1, N + 1):
        if in_degree[idx] == 0:
            heapq.heappush(heap, idx)
    
    while heap:
        problem = heapq.heappop(heap)
        sequence.append(problem)

        for next_problem in graph[problem]:
            in_degree[next_problem] -= 1
            if in_degree[next_problem] == 0:
                heapq.heappush(heap, next_problem)
    
    print(*sequence)

solution()
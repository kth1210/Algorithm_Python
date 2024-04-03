import sys
import heapq
INF = sys.maxsize

def dijkstra(graph, start_node):
    distances = [INF for _ in range(len(graph))]
    queue = []

    heapq.heappush(queue, (start_node, 0))
    distances[start_node] = 0

    while queue:
        current_destination, current_distance = heapq.heappop(queue)

        if current_distance > distances[current_destination]:
            continue

        for next_node, next_distance in graph[current_destination]:
            distance = next_distance + current_distance

            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (next_node, distance))
    
    return distances

def solution():
    N, M, X = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    reversed_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append((end, cost))
        reversed_graph[end].append((start, cost))
    
    distances = dijkstra(graph, X)
    reversed_distances = dijkstra(reversed_graph, X)

    maximum_time = 0
    for idx in range(1, len(distances)):
        time = distances[idx] + reversed_distances[idx]
        maximum_time = max(maximum_time, time)
    
    print(maximum_time)

solution()
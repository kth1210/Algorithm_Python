import sys
import heapq
INF = sys.maxsize

def dijkstra(graph, start_node):
    distances = [INF for _ in range(len(graph) + 1)]
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
    N, M = map(int, sys.stdin.readline().split())
    graph = {}

    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().split())

        if A in graph:
            graph[A].append((B, C))
        else:
            graph[A] = [(B, C)]
        
        if B in graph:
            graph[B].append((A, C))
        else:
            graph[B] = [(A, C)]

    distances = dijkstra(graph, 1)
    print(distances[N])

solution()
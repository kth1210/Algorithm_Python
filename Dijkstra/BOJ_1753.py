import sys
import heapq
INF = sys.maxsize

def dijkstra(graph, start_node):
    distances = [INF for _ in range(len(graph))]
    queue = []

    # 출발지까지의 거리 = 0
    heapq.heappush(queue, (0, start_node))
    distances[start_node] = 0

    while queue:
        # current_destination 까지의 거리가 current_distance
        current_distance, current_destination = heapq.heappop(queue)

        # queue에 들어갔지만 이미 current_destination에 더 빨리 도착했었을 수도 있음
        if distances[current_destination] < current_distance:
            continue

        for next_distance, next_node in graph[current_destination]:
            # 다음 노드까지의 거리
            distance = next_distance + current_distance
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return distances

def solution():
    V, E = map(int, sys.stdin.readline().split())
    start_node = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((w, v))

    distances = dijkstra(graph, start_node)
    # 맨 앞 dump 공간에 대한 보상
    for distance in distances[1:]:
        if distance == INF:
            print('INF')
        else:
            print(distance)

solution()
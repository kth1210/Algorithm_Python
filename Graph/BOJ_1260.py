import sys
from collections import deque

def DFS(graph, start_node, visited):
    visited[start_node] = True
    print(start_node, end = ' ')

    graph[start_node].sort()
    for node in graph[start_node]:
        if not visited[node]:
            DFS(graph, node, visited)

def BFS(graph, start_node, visited):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()
        print(current_node, end = ' ')

        graph[current_node].sort()
        for node in graph[current_node]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

def solution():
    node_count, edge_count, start_node = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(node_count + 1)]

    for _ in range(edge_count):
        first_node, second_node = map(int, sys.stdin.readline().split())

        graph[first_node].append(second_node)
        graph[second_node].append(first_node)

    visited_DFS = [False] * (node_count + 1)
    DFS(graph, start_node, visited_DFS)

    print()
    visited_BFS = [False] * (node_count + 1)
    BFS(graph, start_node, visited_BFS)

solution()
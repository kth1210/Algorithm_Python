import sys
from collections import deque

def BFS(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()

        for next_node in graph[current_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

def solution():
    node_count, edge_count = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(node_count + 1)]
    visited = [False] * (node_count + 1)

    for _ in range(edge_count):
        first_node, second_node = map(int, sys.stdin.readline().split())
        graph[first_node].append(second_node)
        graph[second_node].append(first_node)
    
    count = 0
    for node_idx in range(1, node_count + 1):
        if not visited[node_idx]:
            BFS(graph, visited, node_idx)
            count += 1
    
    print(count)

solution()